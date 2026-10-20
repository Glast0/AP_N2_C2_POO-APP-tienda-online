from negocio.negocio_carritos import (crear_carrito, agregar_item, items_carrito, 
lista_carritos, obtener_carrito, obtener_item, modificar_cantidad_item, carrito_tiene_items, comprar_carrito, eliminar_carrito)
from negocio.negocio_cliente import lista_clientes
from negocio.negocio_productos import lista_productos
from presentacion.presentacion_pedidos import pedir_entero
from negocio.negocio_direccion import lista_direcciones_de_cliente, direccion_es_del_cliente

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

def solicitar_cambio_cantidad_item():
    print('\nCarritos disponibles:')
    lista_carritos()

    carrito = None
    while carrito is None:
        id_carrito = pedir_entero('Ingrese el Id del carrito (0 para cancelar): ')
        if id_carrito == 0:
            print('Operación cancelada.')
            return
        carrito = obtener_carrito(id_carrito)
        if carrito is None:
            print(f'El carrito con Id {id_carrito} no existe. Intente nuevamente.')

    print()
    items_carrito(carrito.id_carrito)

    item = None
    while item is None:
        id_item = pedir_entero('Ingrese el Id del ítem a modificar (0 para cancelar): ')
        if id_item == 0:
            print('Operación cancelada.')
            return
        item = obtener_item(id_item)
        if item is None or item.id_carrito != carrito.id_carrito:
            print(f'El ítem {id_item} no pertenece a ese carrito. Intente nuevamente.')
            item = None

    print(f'Cantidad actual: {item.cantidad}')
    cantidad = pedir_entero('Nueva cantidad: ')
    modificar_cantidad_item(carrito.id_carrito, item.id_item_carrito, cantidad)

def solicitar_compra_carrito():
    print('\nCarritos disponibles:')
    lista_carritos()

    carrito = None
    while carrito is None:
        id_carrito = pedir_entero('Ingrese el Id del carrito a comprar (0 para cancelar): ')
        if id_carrito == 0:
            print('Compra cancelada.')
            return
        carrito = obtener_carrito(id_carrito)
        if carrito is None:
            print(f'El carrito con Id {id_carrito} no existe. Intente nuevamente.')

    if not carrito_tiene_items(carrito.id_carrito):
        print('El carrito está vacío. Agrega productos primero (opción 3 del menú Carritos).')
        return

    print()
    items_carrito(carrito.id_carrito)
    print('(Los precios del carrito son referenciales: el pedido usará el precio actual.)')

    print(f'\nDirecciones del cliente {carrito.id_cliente}:')
    if not lista_direcciones_de_cliente(carrito.id_cliente):
        print('Ese cliente no tiene direcciones. Registra una en el menú Direcciones de entrega.')
        return

    id_direccion = None
    while id_direccion is None:
        candidato = pedir_entero('Ingrese el Id de la dirección de entrega (0 para cancelar): ')
        if candidato == 0:
            print('Compra cancelada.')
            return
        if direccion_es_del_cliente(candidato, carrito.id_cliente):
            id_direccion = candidato
        else:
            print('Esa dirección no existe o no pertenece al cliente. Intente nuevamente.')

    confirmar = input('¿Comprar el carrito? Se creará el pedido y se vaciará el carrito. [s/n]: ')
    if confirmar.strip().lower() != 's':
        print('Compra cancelada.')
        return

    comprar_carrito(carrito.id_carrito, id_direccion)

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