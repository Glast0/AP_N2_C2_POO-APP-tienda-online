from decimal import Decimal, InvalidOperation
from negocio.negocio_productos import (
    crear_producto, lista_productos, obtener_producto, modificar_producto, categoria_existe)
from negocio.negocio_categoria import lista_categorias
from presentacion.presentacion_pedidos import pedir_entero

def solicitar_datos_producto():
    nombre = ''
    while nombre == '':
        nombre = input('Ingrese nombre del producto: ')

    descripcion = input('Ingrese descripción (puede dejarla vacía): ')
    if descripcion == '':
        descripcion = None

    precio = None
    while precio is None:
        try:
            precio = Decimal(input('Ingrese precio: '))
        except InvalidOperation:
            print('Debe ingresar un número (ej: 12990.50).')

    stock = None
    while stock is None:
        try:
            stock = int(input('Ingrese stock disponible: '))
        except ValueError:
            print('Debe ingresar un número entero.')

    print('\nCategorías disponibles:')
    lista_categorias()
    id_categoria = None
    while id_categoria is None:
        try:
            id_categoria = int(input('Ingrese el Id de la categoría: '))
        except ValueError:
            print('Debe ingresar un número entero.')

    crear_producto(nombre, descripcion, precio, stock, id_categoria)

def pedir_decimal_o_mantener(mensaje, actual):
    while True:
        texto = input(mensaje)
        if texto == '':
            return actual
        try:
            return Decimal(texto)
        except InvalidOperation:
            print('Debe ingresar un número (ej: 12990.50).')

def pedir_entero_o_mantener(mensaje, actual):
    while True:
        texto = input(mensaje)
        if texto == '':
            return actual
        try:
            return int(texto)
        except ValueError:
            print('Debe ingresar un número entero.')

def solicitar_modificacion_producto():
    print('\nProductos disponibles:')
    lista_productos()

    producto = None
    while producto is None:
        id_producto = pedir_entero('Ingrese el Id del producto a modificar (0 para cancelar): ')
        if id_producto == 0:
            print('Modificación cancelada.')
            return
        producto = obtener_producto(id_producto)
        if producto is None:
            print(f'El producto con Id {id_producto} no existe. Intente nuevamente.')

    print(f'\nNombre actual: {producto.nombre_producto}')
    nombre = input('Nuevo nombre (Enter para mantener): ')
    if nombre == '':
        nombre = producto.nombre_producto

    print(f'Descripción actual: {producto.descripcion}')
    descripcion = input('Nueva descripción (Enter para mantener, "-" para dejarla vacía): ')
    if descripcion == '':
        descripcion = producto.descripcion
    elif descripcion == '-':
        descripcion = None

    print(f'Precio actual: {producto.precio}')
    precio = pedir_decimal_o_mantener('Nuevo precio (Enter para mantener): ', producto.precio)

    print(f'Stock actual: {producto.stock_disponible}')
    stock = pedir_entero_o_mantener('Nuevo stock (Enter para mantener): ', producto.stock_disponible)

    print('\nCategorías disponibles:')
    lista_categorias()
    print(f'Categoría actual (Id): {producto.id_categoria}')
    id_categoria = None
    while id_categoria is None:
        id_categoria = pedir_entero_o_mantener(
            'Nuevo Id de categoría (Enter para mantener): ', producto.id_categoria)
        if not categoria_existe(id_categoria):
            print(f'La categoría con Id {id_categoria} no existe. Intente nuevamente.')
            id_categoria = None

    modificar_producto(producto.id_producto, nombre, descripcion, precio, stock, id_categoria)