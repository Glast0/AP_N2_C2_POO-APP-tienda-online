from datos.modelos.base import database
from datos.modelos.pedido import Pedido, DetallePedido
from datos.modelos.producto import Producto
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

def guardar_pedido(pedido: Pedido, detalles: list):
    try:
        with database.atomic():
            pedido.save()
            for detalle in detalles:
                detalle.id_pedido = pedido.id_pedido
                detalle.save()

                # Descuento condicional: solo resta si todavía alcanza el stock
                filas = (Producto
                         .update(stock_disponible=Producto.stock_disponible - detalle.cantidad)
                         .where((Producto.id_producto == detalle.id_producto) &
                                (Producto.stock_disponible >= detalle.cantidad))
                         .execute())
                if filas == 0:
                    raise StockInsuficiente(detalle.id_producto)
        print(f'Pedido guardado con éxito con Id: {pedido.id_pedido}.')
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

def pedidos_en_curso_de_cliente(id_cliente: int):
    return Pedido.select().where(
        (Pedido.id_cliente == id_cliente) & (Pedido.id_estado_pedido.in_([1, 2, 3, 4])))

def pedidos_en_curso_de_direccion(id_direccion: int):
    return Pedido.select().where(
        (Pedido.id_direccion_entrega == id_direccion) & (Pedido.id_estado_pedido.in_([1, 2, 3, 4])))