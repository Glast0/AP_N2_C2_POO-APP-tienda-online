from datos.modelos.direccion_entrega import DireccionEntrega
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_direcciones():
    direcciones = DireccionEntrega.select()
    if direcciones:
        return direcciones

def guardar_direccion(direccion: DireccionEntrega):
    try:
        resultado = direccion.save()
        if resultado == 1:
            print(f'Dirección guardada con éxito con Id: {direccion.id_direccion_entrega}.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

def buscar_direccion(id_direccion: int):
    return DireccionEntrega.get_or_none(DireccionEntrega.id_direccion_entrega == id_direccion)

def actualizar_direccion(direccion: DireccionEntrega):
    try:
        direccion.save()
        print(f'Dirección {direccion.id_direccion_entrega} actualizada con éxito.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")

def direcciones_de_cliente(id_cliente: int):
    return DireccionEntrega.select().where(DireccionEntrega.id_cliente == id_cliente)


def deshabilitar_direccion(direccion: DireccionEntrega):
    try:
        direccion.habilitado = 0
        direccion.save()
        print(f'Dirección {direccion.id_direccion_entrega} eliminada con éxito.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudo eliminar por un error genérico: {e}")