from datetime import date
from negocio.negocio_envio import crear_envio
from negocio.negocio_pedido import lista_pedidos
from presentacion.presentacion_pedidos import pedir_entero

def solicitar_datos_envio():
    print('\nPedidos disponibles:')
    lista_pedidos()
    id_pedido = pedir_entero('Ingrese el Id del pedido a despachar: ')

    transportista = ''
    while transportista == '':
        transportista = input('Ingrese transportista: ')

    # El número de seguimiento es opcional (null=True en el modelo)
    seguimiento = input('Ingrese número de seguimiento (puede dejarlo vacío): ')
    if seguimiento == '':
        seguimiento = None

    fecha_estimada = None
    while fecha_estimada is None:
        try:
            fecha_estimada = date.fromisoformat(input('Ingrese fecha de entrega estimada (AAAA-MM-DD): '))
        except ValueError:
            print('Formato inválido. Ejemplo: 2026-10-20')

    crear_envio(id_pedido, transportista, seguimiento, fecha_estimada)