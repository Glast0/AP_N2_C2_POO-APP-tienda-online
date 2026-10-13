from negocio.negocio_cliente import crear_cliente

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