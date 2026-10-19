from datetime import date
from negocio.negocio_envio import crear_envio, lista_envios, obtener_envio, registrar_entrega
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

def solicitar_entrega_envio():
    print('\nEnvíos registrados:')
    lista_envios()

    envio = None
    while envio is None:
        id_envio = pedir_entero('Ingrese el Id del envío entregado (0 para cancelar): ')
        if id_envio == 0:
            print('Operación cancelada.')
            return
        envio = obtener_envio(id_envio)
        if envio is None:
            print(f'El envío con Id {id_envio} no existe. Intente nuevamente.')

    fecha_real = None
    while fecha_real is None:
        texto = input('Fecha de entrega real (AAAA-MM-DD, Enter para hoy): ')
        if texto == '':
            fecha_real = date.today()
            break
        try:
            fecha_real = date.fromisoformat(texto)
        except ValueError:
            print('Formato inválido. Ejemplo: 2026-10-20')

    confirmar = input(f'¿Registrar la entrega del envío {envio.id_envio} '
                      f'(pedido {envio.id_pedido}) el {fecha_real}? [s/n]: ').strip().lower()
    if confirmar != 's':
        print('Operación cancelada.')
        return

    registrar_entrega(envio.id_envio, fecha_real)