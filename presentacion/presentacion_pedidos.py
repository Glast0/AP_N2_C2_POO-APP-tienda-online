from negocio.negocio_pedido import crear_pedido, detalle_pedido
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