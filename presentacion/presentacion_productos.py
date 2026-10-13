from decimal import Decimal, InvalidOperation
from negocio.negocio_productos import crear_producto
from negocio.negocio_categoria import lista_categorias

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