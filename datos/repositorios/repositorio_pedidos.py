from datos.modelos.pedido import Pedido, DetallePedido, database
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

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
        # atomic(): si algo falla, se deshace todo (cabecera y detalles)
        with database.atomic():
            pedido.save()
            for detalle in detalles:
                detalle.id_pedido = pedido.id_pedido
                detalle.save()
        print(f'Pedido guardado con éxito con Id: {pedido.id_pedido}.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")