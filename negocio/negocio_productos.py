from datos.repositorios.repositorio_productos import (
    listado_productos, guardar_producto, buscar_producto, actualizar_producto, deshabilitar_producto)
from datos.repositorios.repositorio_categorias import buscar_categoria
from prettytable import PrettyTable
from datos.modelos.producto import Producto
from decimal import Decimal

def lista_productos():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Producto', 'Descripción', 'Precio', 'Stock', 'Id categoría', 'Habilitado']

    productos = listado_productos()
    if productos:
        for p in productos:
            tabla.add_row([p.id_producto, p.nombre_producto, p.descripcion, p.precio,
                           p.stock_disponible, p.id_categoria,
                           ('Deshabilitado', 'Habilitado')[p.habilitado]])
        print(tabla)

def crear_producto(nombre_producto, descripcion, precio, stock, id_categoria):
    # Reglas de negocio
    if not precio.is_finite():
        print('El precio ingresado no es válido. Producto NO guardado.')
        return
    if precio > 99999999.99:
        print('El precio supera el máximo permitido (99.999.999,99). Producto NO guardado.')
        return
    if stock > 1000000:
        print('El stock supera el máximo permitido (1.000.000). Producto NO guardado.')
        return
    if precio <= 0:
        print('El precio debe ser mayor a 0. Producto NO guardado.')
        return
    if stock < 0:
        print('El stock no puede ser negativo. Producto NO guardado.')
        return
    if buscar_categoria(id_categoria) is None:
        print(f'La categoría con Id {id_categoria} no existe. Producto NO guardado.')
        return

    nuevo = Producto()
    nuevo.nombre_producto = nombre_producto
    nuevo.descripcion = descripcion
    nuevo.precio = precio
    nuevo.stock_disponible = stock
    nuevo.id_categoria = id_categoria
    guardar_producto(nuevo)

def categoria_existe(id_categoria):
    return buscar_categoria(id_categoria) is not None

def obtener_producto(id_producto):
    return buscar_producto(id_producto)

def modificar_producto(id_producto, nombre_producto, descripcion, precio, stock, id_categoria):
    producto = buscar_producto(id_producto)
    if producto is None:
        print(f'El producto con Id {id_producto} no existe. Cambios NO guardados.')
        return
    if nombre_producto.strip() == '':
        print('El nombre no puede quedar vacío. Cambios NO guardados.')
        return
    if not precio.is_finite() or precio <= 0:
        print('El precio debe ser un número mayor a 0. Cambios NO guardados.')
        return
    if precio > Decimal('99999999.99'):
        print('El precio supera el máximo permitido (99.999.999,99). Cambios NO guardados.')
        return
    if stock < 0:
        print('El stock no puede ser negativo. Cambios NO guardados.')
        return
    if stock > 1000000:
        print('El stock supera el máximo permitido (1.000.000). Cambios NO guardados.')
        return
    if buscar_categoria(id_categoria) is None:
        print(f'La categoría con Id {id_categoria} no existe. Cambios NO guardados.')
        return

    if (nombre_producto == producto.nombre_producto and descripcion == producto.descripcion
            and precio == producto.precio and stock == producto.stock_disponible
            and id_categoria == producto.id_categoria):
        print('No hubo cambios. Nada que actualizar.')
        return

    producto.nombre_producto = nombre_producto
    producto.descripcion = descripcion
    producto.precio = precio
    producto.stock_disponible = stock
    producto.id_categoria = id_categoria
    actualizar_producto(producto)

def eliminar_producto(id_producto):
    producto = buscar_producto(id_producto)
    if producto is None:
        print(f'El producto con Id {id_producto} no existe. Producto NO eliminado.')
        return
    if producto.habilitado == 0:
        print('El producto ya está deshabilitado. Nada que hacer.')
        return

    deshabilitar_producto(producto)