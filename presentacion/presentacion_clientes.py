from negocio.negocio_cliente import crear_cliente, lista_clientes, obtener_cliente, modificar_cliente,eliminar_cliente
from presentacion.presentacion_pedidos import pedir_entero

def solicitar_datos_cliente():
    nombre = rut = email = ''

    while nombre == '':
        nombre = input('Ingrese nombre del cliente: ')
    while rut == '':
        rut = input('Ingrese RUT (ej: 12345678-9): ')
    while email == '':
        email = input('Ingrese email: ')

    # El teléfono es opcional (null=True en el modelo)
    telefono = input('Ingrese teléfono (puede dejarlo vacío): ')
    if telefono == '':
        telefono = None

    crear_cliente(nombre, rut, email, telefono)

def solicitar_modificacion_cliente():
    print('\nClientes disponibles:')
    lista_clientes()

    cliente = None
    while cliente is None:
        id_cliente = pedir_entero('Ingrese el Id del cliente a modificar (0 para cancelar): ')
        if id_cliente == 0:
            print('Modificación cancelada.')
            return
        cliente = obtener_cliente(id_cliente)
        if cliente is None:
            print(f'El cliente con Id {id_cliente} no existe. Intente nuevamente.')

    print(f'\nNombre actual: {cliente.nombre}')
    nombre = input('Nuevo nombre (Enter para mantener): ')
    if nombre == '':
        nombre = cliente.nombre

    print(f'RUT actual: {cliente.rut}')
    rut = input('Nuevo RUT (Enter para mantener): ')
    if rut == '':
        rut = cliente.rut

    print(f'Email actual: {cliente.email}')
    email = input('Nuevo email (Enter para mantener): ')
    if email == '':
        email = cliente.email

    print(f'Teléfono actual: {cliente.telefono}')
    telefono = input('Nuevo teléfono (Enter para mantener, "-" para dejarlo vacío): ')
    if telefono == '':
        telefono = cliente.telefono
    elif telefono == '-':
        telefono = None

    modificar_cliente(cliente.id_cliente, nombre, rut, email, telefono)

def solicitar_eliminacion_cliente():
    print('\nClientes disponibles:')
    lista_clientes()

    cliente = None
    while cliente is None:
        id_cliente = pedir_entero('Ingrese el Id del cliente a eliminar (0 para cancelar): ')
        if id_cliente == 0:
            print('Eliminación cancelada.')
            return
        cliente = obtener_cliente(id_cliente)
        if cliente is None:
            print(f'El cliente con Id {id_cliente} no existe. Intente nuevamente.')

    confirmar = input(f'¿Eliminar al cliente "{cliente.nombre}"? [s/n]: ').strip().lower()
    if confirmar != 's':
        print('Eliminación cancelada.')
        return

    eliminar_cliente(cliente.id_cliente)