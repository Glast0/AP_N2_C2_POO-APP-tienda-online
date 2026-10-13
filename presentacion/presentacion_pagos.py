from decimal import Decimal, InvalidOperation
from negocio.negocio_pago import crear_pago, METODOS_PAGO
from negocio.negocio_pedido import lista_pedidos
from presentacion.presentacion_pedidos import pedir_entero

def solicitar_datos_pago():
    print('\nPedidos disponibles:')
    lista_pedidos()
    id_pedido = pedir_entero('Ingrese el Id del pedido a pagar: ')

    monto = None
    while monto is None:
        try:
            monto = Decimal(input('Ingrese el monto a pagar: '))
        except InvalidOperation:
            print('Debe ingresar un número (ej: 12990.50).')

    print('\nMétodos de pago:')
    for i, metodo in enumerate(METODOS_PAGO, start=1):
        print(f'[{i}] - {metodo}')
    opcion = 0
    while opcion < 1 or opcion > len(METODOS_PAGO):
        opcion = pedir_entero(f'Elija el método [1-{len(METODOS_PAGO)}]: ')

    crear_pago(id_pedido, monto, METODOS_PAGO[opcion - 1])