from negocio.negocio_direccion import (
    crear_direccion, lista_direcciones, obtener_direccion, modificar_direccion,
    eliminar_direccion)
from negocio.negocio_cliente import lista_clientes
from presentacion.presentacion_pedidos import pedir_entero

def solicitar_datos_direccion():
    print('\nClientes disponibles:')
    lista_clientes()
    id_cliente = None
    while id_cliente is None:
        try:
            id_cliente = int(input('Ingrese el Id del cliente: '))
        except ValueError:
            print('Debe ingresar un número entero.')

    calle = numero = comuna = ciudad = ''
    while calle == '':
        calle = input('Ingrese calle: ')
    while numero == '':
        numero = input('Ingrese número: ')
    while comuna == '':
        comuna = input('Ingrese comuna: ')
    while ciudad == '':
        ciudad = input('Ingrese ciudad: ')

    crear_direccion(id_cliente, calle, numero, comuna, ciudad)

def solicitar_modificacion_direccion():
    print('\nDirecciones disponibles:')
    lista_direcciones()

    direccion = None
    while direccion is None:
        id_direccion = pedir_entero('Ingrese el Id de la dirección a modificar (0 para cancelar): ')
        if id_direccion == 0:
            print('Modificación cancelada.')
            return
        direccion = obtener_direccion(id_direccion)
        if direccion is None:
            print(f'La dirección con Id {id_direccion} no existe. Intente nuevamente.')

    print(f'\nCalle actual: {direccion.calle}')
    calle = input('Nueva calle (Enter para mantener): ') or direccion.calle

    print(f'Número actual: {direccion.numero}')
    numero = input('Nuevo número (Enter para mantener): ') or direccion.numero

    print(f'Comuna actual: {direccion.comuna}')
    comuna = input('Nueva comuna (Enter para mantener): ') or direccion.comuna

    print(f'Ciudad actual: {direccion.ciudad}')
    ciudad = input('Nueva ciudad (Enter para mantener): ') or direccion.ciudad

    modificar_direccion(direccion.id_direccion_entrega, calle, numero, comuna, ciudad)

def solicitar_eliminacion_direccion():
    print('\nDirecciones disponibles:')
    lista_direcciones()

    direccion = None
    while direccion is None:
        id_direccion = pedir_entero('Ingrese el Id de la dirección a eliminar (0 para cancelar): ')
        if id_direccion == 0:
            print('Eliminación cancelada.')
            return
        direccion = obtener_direccion(id_direccion)
        if direccion is None:
            print(f'La dirección con Id {id_direccion} no existe. Intente nuevamente.')

    confirmar = input(f'¿Eliminar la dirección "{direccion.calle} {direccion.numero}"? [s/n]: ').strip().lower()
    if confirmar != 's':
        print('Eliminación cancelada.')
        return

    eliminar_direccion(direccion.id_direccion_entrega)