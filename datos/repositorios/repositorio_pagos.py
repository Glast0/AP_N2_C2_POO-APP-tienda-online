from datos.modelos.pago import Pago
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_pagos():
    pagos = Pago.select()
    if pagos:
        return pagos

def pagos_de_pedido(id_pedido: int):
    return Pago.select().where(Pago.id_pedido == id_pedido)

def guardar_pago(pago: Pago):
    try:
        resultado = pago.save()
        if resultado == 1:
            print(f'Pago guardado con éxito con Id: {pago.id_pago}.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")