from datetime import date
from prettytable import PrettyTable
from datos.repositorios.repositorio_carritos import (
    listado_carritos, buscar_carrito, buscar_carrito_de_cliente, listado_items,
    buscar_item_en_carrito, guardar_carrito, guardar_item)
from datos.repositorios.repositorio_clientes import buscar_cliente
from datos.repositorios.repositorio_productos import buscar_producto
from datos.modelos.carritos import Carrito, ItemCarrito

def lista_carritos():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Id cliente', 'Fecha creación', 'Habilitado']

    carritos = listado_carritos()
    if carritos:
        for c in carritos:
            tabla.add_row([c.id_carrito, c.id_cliente, c.fecha_creacion,
                           ('Deshabilitado', 'Habilitado')[c.habilitado]])
        print(tabla)

def items_carrito(id_carrito):
    if buscar_carrito(id_carrito) is None:
        print(f'El carrito con Id {id_carrito} no existe.')
        return

    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Id producto', 'Cantidad', 'Precio unitario', 'Subtotal']
    total = 0
    for i in listado_items(id_carrito):
        subtotal = i.cantidad * i.precio_unitario
        total += subtotal
        tabla.add_row([i.id_item_carrito, i.id_producto, i.cantidad,
                       i.precio_unitario, subtotal])
    print(tabla)
    print(f'Total del carrito: {total}')

def crear_carrito(id_cliente):
    # Reglas de negocio
    if buscar_cliente(id_cliente) is None:
        print(f'El cliente con Id {id_cliente} no existe. Carrito NO guardado.')
        return
    if buscar_carrito_de_cliente(id_cliente) is not None:
        print(f'El cliente {id_cliente} ya tiene un carrito. Carrito NO guardado.')
        return

    nuevo = Carrito()
    nuevo.id_cliente = id_cliente
    nuevo.fecha_creacion = date.today()
    guardar_carrito(nuevo)

def agregar_item(id_carrito, id_producto, cantidad):
    # Reglas de negocio
    if buscar_carrito(id_carrito) is None:
        print(f'El carrito con Id {id_carrito} no existe. Producto NO agregado.')
        return

    producto = buscar_producto(id_producto)
    if producto is None:
        print(f'El producto con Id {id_producto} no existe. Producto NO agregado.')
        return
    if cantidad <= 0:
        print('La cantidad debe ser mayor a 0. Producto NO agregado.')
        return
    if cantidad > producto.stock_disponible:
        print(f'Stock insuficiente para "{producto.nombre_producto}" '
              f'(disponible: {producto.stock_disponible}). Producto NO agregado.')
        return
    if buscar_item_en_carrito(id_carrito, id_producto) is not None:
        print('Ese producto ya está en el carrito. Producto NO agregado.')
        return

    nuevo = ItemCarrito()
    nuevo.id_carrito = id_carrito
    nuevo.id_producto = id_producto
    nuevo.cantidad = cantidad
    nuevo.precio_unitario = producto.precio  # precio del momento
    guardar_item(nuevo)