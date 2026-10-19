from negocio.negocio_carritos import crear_carrito, agregar_item, items_carrito, lista_carritos, obtener_carrito, obtener_item, modificar_cantidad_item
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