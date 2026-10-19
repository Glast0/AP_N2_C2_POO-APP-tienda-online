from negocio.negocio_pedido import (
    crear_pedido, detalle_pedido, lista_pedidos, obtener_pedido,
    avanzar_estado_pedido, cancelar_pedido, ESTADOS, TRANSICIONES)
from negocio.negocio_cliente import lista_clientes
from negocio.negocio_direccion import lista_direcciones
from negocio.negocio_productos import lista_productos

def pedir_entero(mensaje):
    valor = None
    while valor is None:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print('Debe ingresar un número entero.')
    return valor

def solicitar_datos_pedido():
    print('\nClientes disponibles:')
    lista_clientes()
    id_cliente = pedir_entero('Ingrese el Id del cliente: ')

    print('\nDirecciones disponibles:')
    lista_direcciones()
    id_direccion = pedir_entero('Ingrese el Id de la dirección de entrega: ')

    items = []
    print('\nProductos disponibles:')
    lista_productos()
    while True:
        id_producto = pedir_entero('Ingrese el Id del producto: ')
        cantidad = pedir_entero('Ingrese la cantidad: ')
        items.append((id_producto, cantidad))

        otro = input('¿Agregar otro producto? [s/n]: ').strip().lower()
        if otro != 's':
            break

    crear_pedido(id_cliente, id_direccion, items)

def solicitar_detalle_pedido():
    id_pedido = pedir_entero('Ingrese el Id del pedido: ')
    detalle_pedido(id_pedido)

def pedir_pedido_existente(mensaje):
    """Pide un Id hasta que exista (0 cancela y devuelve None)."""
    while True:
        id_pedido = pedir_entero(mensaje)
        if id_pedido == 0:
            return None
        pedido = obtener_pedido(id_pedido)
        if pedido is not None:
            return pedido
        print(f'El pedido con Id {id_pedido} no existe. Intente nuevamente.')

def solicitar_avance_estado_pedido():
    print('\nPedidos disponibles:')
    lista_pedidos()

    pedido = pedir_pedido_existente('Ingrese el Id del pedido a avanzar (0 para cancelar): ')
    if pedido is None:
        print('Operación cancelada.')
        return

    actual = pedido.id_estado_pedido
    if actual in TRANSICIONES:
        confirmar = input(f'¿Pasar el pedido {pedido.id_pedido} de {ESTADOS[actual]} '
                          f'a {ESTADOS[TRANSICIONES[actual]]}? [s/n]: ').strip().lower()
        if confirmar != 's':
            print('Operación cancelada.')
            return

    avanzar_estado_pedido(pedido.id_pedido)

def solicitar_cancelacion_pedido():
    print('\nPedidos disponibles:')
    lista_pedidos()

    pedido = pedir_pedido_existente('Ingrese el Id del pedido a cancelar (0 para volver): ')
    if pedido is None:
        print('Operación cancelada.')
        return

    confirmar = input(f'¿Cancelar el pedido {pedido.id_pedido}? Se devolverá el stock '
                      'y se ajustarán sus pagos. [s/n]: ').strip().lower()
    if confirmar != 's':
        print('Operación cancelada.')
        return

    cancelar_pedido(pedido.id_pedido)