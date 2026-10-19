from datos.modelos.envio import Envio
from peewee import IntegrityError, OperationalError, DataError, PeeweeException
from datos.modelos.base import database
from datos.modelos.pedido import Pedido

def listado_envios():
    envios = Envio.select()
    if envios:
        return envios

def buscar_envio_de_pedido(id_pedido: int):
    return Envio.get_or_none(Envio.id_pedido == id_pedido)

def guardar_envio(envio: Envio):
    try:
        resultado = envio.save()
        if resultado == 1:
            print(f'Envío guardado con éxito con Id: {envio.id_envio}.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea (¿el pedido ya tiene envío?): {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

class EntregaNoRegistrable(Exception):
    pass

def buscar_envio(id_envio: int):
    return Envio.get_or_none(Envio.id_envio == id_envio)

def registrar_entrega_en_bd(id_envio: int, id_pedido: int, fecha_real):
    try:
        with database.atomic():
            # Solo si el envío todavía no tiene entrega registrada
            filas = (Envio
                     .update(fecha_entrega_real=fecha_real)
                     .where((Envio.id_envio == id_envio) &
                            (Envio.fecha_entrega_real.is_null(True)))
                     .execute())
            if filas == 0:
                raise EntregaNoRegistrable()

            # Solo si el pedido sigue ENVIADO (4) -> ENTREGADO (5)
            filas_pedido = (Pedido
                            .update(id_estado_pedido=5)
                            .where((Pedido.id_pedido == id_pedido) &
                                   (Pedido.id_estado_pedido == 4))
                            .execute())
            if filas_pedido == 0:
                raise EntregaNoRegistrable()
        print(f'Entrega registrada. El pedido {id_pedido} pasó a ENTREGADO.')
    except EntregaNoRegistrable:
        print('El envío o el pedido cambió mientras tanto. Entrega NO registrada.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")