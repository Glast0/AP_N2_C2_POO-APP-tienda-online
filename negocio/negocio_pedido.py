from datetime import date
from prettytable import PrettyTable
from datos.repositorios.repositorio_pedidos import (
    listado_pedidos, listado_detalle, buscar_pedido, guardar_pedido)
from datos.repositorios.repositorio_clientes import buscar_cliente
from datos.repositorios.repositorio_direcciones import buscar_direccion
from datos.repositorios.repositorio_productos import buscar_producto
from datos.modelos.pedido import Pedido, DetallePedido

ESTADOS = {1: 'CREADO', 2: 'CONFIRMADO', 3: 'EN_PREPARACION',
           4: 'ENVIADO', 5: 'ENTREGADO', 6: 'CANCELADO'}

def lista_pedidos():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Fecha', 'Id cliente', 'Id dirección', 'Total', 'Estado']

    pedidos = listado_pedidos()
    if pedidos:
        for p in pedidos:
            tabla.add_row([p.id_pedido, p.fecha, p.id_cliente, p.id_direccion_entrega,
                           p.total, ESTADOS.get(p.id_estado_pedido, p.id_estado_pedido)])
        print(tabla)

def detalle_pedido(id_pedido):
    if buscar_pedido(id_pedido) is None:
        print(f'El pedido con Id {id_pedido} no existe.')
        return

    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Id producto', 'Cantidad', 'Precio unitario', 'Subtotal']
    for d in listado_detalle(id_pedido):
        tabla.add_row([d.id_detalle_pedido, d.id_producto, d.cantidad,
                       d.precio_unitario, d.cantidad * d.precio_unitario])
    print(tabla)

def crear_pedido(id_cliente, id_direccion, items):
    """items es una lista de tuplas (id_producto, cantidad)."""
    # Reglas de negocio
    if buscar_cliente(id_cliente) is None:
        print(f'El cliente con Id {id_cliente} no existe. Pedido NO guardado.')
        return

    direccion = buscar_direccion(id_direccion)
    if direccion is None:
        print(f'La dirección con Id {id_direccion} no existe. Pedido NO guardado.')
        return
    if direccion.id_cliente != id_cliente:
        print('Esa dirección no pertenece al cliente indicado. Pedido NO guardado.')
        return

    if not items:
        print('El pedido no tiene productos. Pedido NO guardado.')
        return

    # Si un producto se repite, se suman sus cantidades
    agrupados = {}
    for id_producto, cantidad in items:
        if cantidad <= 0:
            print('La cantidad debe ser mayor a 0. Pedido NO guardado.')
            return
        agrupados[id_producto] = agrupados.get(id_producto, 0) + cantidad

    detalles = []
    total = 0
    for id_producto, cantidad in agrupados.items():
        producto = buscar_producto(id_producto)
        if producto is None:
            print(f'El producto con Id {id_producto} no existe. Pedido NO guardado.')
            return
        if cantidad > producto.stock_disponible:
            print(f'Stock insuficiente para "{producto.nombre_producto}" '
                  f'(disponible: {producto.stock_disponible}). Pedido NO guardado.')
            return

        detalle = DetallePedido()
        detalle.id_producto = id_producto
        detalle.cantidad = cantidad
        detalle.precio_unitario = producto.precio
        detalles.append(detalle)
        total += cantidad * producto.precio

    pedido = Pedido()
    pedido.fecha = date.today()
    pedido.total = total
    pedido.id_cliente = id_cliente
    pedido.id_direccion_entrega = id_direccion
    guardar_pedido(pedido, detalles)