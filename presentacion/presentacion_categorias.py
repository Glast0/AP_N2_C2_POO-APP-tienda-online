from negocio.negocio_categoria import crear_categoria, lista_categorias, obtener_categoria, modificar_categoria, eliminar_categoria
from presentacion.presentacion_pedidos import pedir_entero

def solicitar_datos_categoria():
    nombre = ''
    while nombre == '':
        nombre = input('Ingrese nombre de la categoría: ')

    # La descripción es opcional (null=True en el modelo)
    descripcion = input('Ingrese descripción (puede dejarla vacía): ')
    if descripcion == '':
        descripcion = None

    crear_categoria(nombre, descripcion)

def solicitar_modificacion_categoria():
    print('\nCategorías disponibles:')
    lista_categorias()

    categoria = None
    while categoria is None:
        id_categoria = pedir_entero('Ingrese el Id de la categoría a modificar (0 para cancelar): ')
        if id_categoria == 0:
            print('Modificación cancelada.')
            return
        categoria = obtener_categoria(id_categoria)
        if categoria is None:
            print(f'La categoría con Id {id_categoria} no existe. Intente nuevamente.')

    print(f'\nNombre actual: {categoria.nombre_categoria}')
    nombre = input('Nuevo nombre (Enter para mantener): ')
    if nombre == '':
        nombre = categoria.nombre_categoria

    print(f'Descripción actual: {categoria.descripcion}')
    descripcion = input('Nueva descripción (Enter para mantener, "-" para dejarla vacía): ')
    if descripcion == '':
        descripcion = categoria.descripcion
    elif descripcion == '-':
        descripcion = None

    modificar_categoria(categoria.id_categoria, nombre, descripcion)

def solicitar_eliminacion_categoria():
    print('\nCategorías disponibles:')
    lista_categorias()

    categoria = None
    while categoria is None:
        id_categoria = pedir_entero('Ingrese el Id de la categoría a eliminar (0 para cancelar): ')
        if id_categoria == 0:
            print('Eliminación cancelada.')
            return
        categoria = obtener_categoria(id_categoria)
        if categoria is None:
            print(f'La categoría con Id {id_categoria} no existe. Intente nuevamente.')

    confirmar = input(f'¿Eliminar la categoría "{categoria.nombre_categoria}"? [s/n]: ').strip().lower()
    if confirmar != 's':
        print('Eliminación cancelada.')
        return

    eliminar_categoria(categoria.id_categoria)
