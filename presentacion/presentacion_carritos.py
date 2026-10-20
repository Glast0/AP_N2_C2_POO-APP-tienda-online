from negocio.negocio_carritos import (
    crear_carrito, agregar_item, items_carrito, lista_carritos, eliminar_carrito)
from negocio.negocio_cliente import lista_clientes
from negocio.negocio_productos import lista_productos
from presentacion.presentacion_pedidos import pedir_entero

def solicitar_datos_carrito():
    print('\nClientes disponibles:')
    lista_clientes()
    id_cliente = pedir_entero('Ingrese el Id del cliente: ')
    crear_carrito(id_cliente)

def solicitar_datos_item():
    print('\nCarritos disponibles:')
    lista_carritos()
    id_carrito = pedir_entero('Ingrese el Id del carrito: ')

    print('\nProductos disponibles:')
    lista_productos()
    id_producto = pedir_entero('Ingrese el Id del producto: ')
    cantidad = pedir_entero('Ingrese la cantidad: ')

    agregar_item(id_carrito, id_producto, cantidad)

def solicitar_items_carrito():
    id_carrito = pedir_entero('Ingrese el Id del carrito: ')
    items_carrito(id_carrito)

def solicitar_eliminacion_carrito():
    print('\nCarritos disponibles:')
    lista_carritos()

    id_carrito = pedir_entero('Ingrese el Id del carrito a eliminar (0 para cancelar): ')
    if id_carrito == 0:
        print('Eliminación cancelada.')
        return

    confirmar = input(f'¿Eliminar el carrito {id_carrito} y todos sus productos? [s/n]: ').strip().lower()
    if confirmar != 's':
        print('Eliminación cancelada.')
        return

    eliminar_carrito(id_carrito)