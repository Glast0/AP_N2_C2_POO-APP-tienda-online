from datos.modelos.base import database
from datos.modelos.pago import Pago
from datos.modelos.pedido import Pedido, DetallePedido
from datos.modelos.producto import Producto
from datos.modelos.carritos import ItemCarrito
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

class StockInsuficiente(Exception):
    pass

def listado_pedidos():
    pedidos = Pedido.select()
    if pedidos:
        return pedidos

def listado_detalle(id_pedido: int):
    return DetallePedido.select().where(DetallePedido.id_pedido == id_pedido)

def buscar_pedido(id_pedido: int):
    return Pedido.get_or_none(Pedido.id_pedido == id_pedido)

def guardar_pedido(pedido: Pedido, detalles: list, ids_items_carrito=None):
    try:
        with database.atomic():
            pedido.save()
            for detalle in detalles:
                detalle.id_pedido = pedido.id_pedido
                detalle.save()

                filas = (Producto
                         .update(stock_disponible=Producto.stock_disponible - detalle.cantidad)
                         .where((Producto.id_producto == detalle.id_producto) &
                                (Producto.stock_disponible >= detalle.cantidad))
                         .execute())
                if filas == 0:
                    raise StockInsuficiente(detalle.id_producto)

            # Si viene de un carrito, se sacan de ahí los ítems comprados (borrado real)
            if ids_items_carrito:
                (ItemCarrito
                 .delete()
                 .where(ItemCarrito.id_item_carrito.in_(ids_items_carrito))
                 .execute())
        print(f'Pedido guardado con éxito con Id: {pedido.id_pedido}.')
        if ids_items_carrito:
            print('Los productos comprados salieron del carrito.')
    except StockInsuficiente as e:
        print(f'Stock insuficiente para el producto Id {e}. Pedido NO guardado.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

class EstadoPedidoCambiado(Exception):
    pass

def cambiar_estado_pedido_en_bd(id_pedido: int, estado_actual: int, estado_nuevo: int):
    try:
        # Cambio condicional: solo si el pedido sigue en el estado que vimos
        filas = (Pedido
                 .update(id_estado_pedido=estado_nuevo)
                 .where((Pedido.id_pedido == id_pedido) &
                        (Pedido.id_estado_pedido == estado_actual))
                 .execute())
        if filas == 0:
            raise EstadoPedidoCambiado()
        print(f'Pedido {id_pedido} actualizado con éxito.')
    except EstadoPedidoCambiado:
        print('El estado del pedido cambió mientras tanto. Pedido NO modificado.')
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")

def cancelar_pedido_en_bd(id_pedido: int, estados_cancelables: tuple):
    try:
        with database.atomic():
            # 1. Pasar a CANCELADO, solo si sigue en un estado cancelable
            filas = (Pedido
                     .update(id_estado_pedido=6)
                     .where((Pedido.id_pedido == id_pedido) &
                            (Pedido.id_estado_pedido.in_(estados_cancelables)))
                     .execute())
            if filas == 0:
                raise EstadoPedidoCambiado()

            # 2. Devolver el stock de cada producto del detalle
            for d in listado_detalle(id_pedido):
                (Producto
                 .update(stock_disponible=Producto.stock_disponible + d.cantidad)
                 .where(Producto.id_producto == d.id_producto)
                 .execute())

            # 3. Pagos: pendientes -> RECHAZADO, aprobados -> REEMBOLSADO
            (Pago.update(id_estado_pago=3)
             .where((Pago.id_pedido == id_pedido) & (Pago.id_estado_pago == 1))
             .execute())
            (Pago.update(id_estado_pago=4)
             .where((Pago.id_pedido == id_pedido) & (Pago.id_estado_pago == 2))
             .execute())
        print(f'Pedido {id_pedido} cancelado. Stock devuelto y pagos ajustados.')
    except EstadoPedidoCambiado:
        print('El pedido ya no está en un estado cancelable. Pedido NO modificado.')
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")

def pedidos_en_curso_de_direccion(id_direccion: int):
    return Pedido.select().where(
        (Pedido.id_direccion_entrega == id_direccion) & (Pedido.id_estado_pedido.in_([1, 2, 3, 4])))

def pedidos_en_curso_de_cliente(id_cliente: int):
    return Pedido.select().where(
        (Pedido.id_cliente == id_cliente) & (Pedido.id_estado_pedido.in_([1, 2, 3, 4])))