from negocio.negocio_direccion import crear_direccion
from negocio.negocio_cliente import lista_clientes

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