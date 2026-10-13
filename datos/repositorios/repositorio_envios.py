from datos.modelos.envio import Envio
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

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