from datos.modelos.pago import Pago
from peewee import IntegrityError, OperationalError, DataError, PeeweeException
from decimal import Decimal
from datos.modelos.base import database
from datos.modelos.pedido import Pedido

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

class PagoNoPendiente(Exception):
    pass

def buscar_pago(id_pago: int):
    return Pago.get_or_none(Pago.id_pago == id_pago)

def aprobar_pago_en_bd(id_pago: int, id_pedido: int):
    try:
        with database.atomic():
            # Cambio condicional: solo si el pago sigue PENDIENTE
            filas = (Pago
                     .update(id_estado_pago=2)
                     .where((Pago.id_pago == id_pago) & (Pago.id_estado_pago == 1))
                     .execute())
            if filas == 0:
                raise PagoNoPendiente()

            # Dentro de la transacción ya se ve el pago recién aprobado
            pedido = Pedido.get_by_id(id_pedido)
            aprobado = sum((p.monto for p in pagos_de_pedido(id_pedido)
                            if p.id_estado_pago == 2), Decimal('0'))

            confirmado = False
            if aprobado >= pedido.total:
                filas_pedido = (Pedido
                                .update(id_estado_pedido=2)
                                .where((Pedido.id_pedido == id_pedido) &
                                       (Pedido.id_estado_pedido == 1))
                                .execute())
                confirmado = filas_pedido == 1

        print(f'Pago {id_pago} aprobado con éxito.')
        if confirmado:
            print(f'El pedido {id_pedido} quedó pagado completo y pasó a CONFIRMADO.')
    except PagoNoPendiente:
        print('El pago ya no está PENDIENTE. Pago NO modificado.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")

def rechazar_pago_en_bd(id_pago: int):
    try:
        filas = (Pago
                 .update(id_estado_pago=3)
                 .where((Pago.id_pago == id_pago) & (Pago.id_estado_pago == 1))
                 .execute())
        if filas == 0:
            raise PagoNoPendiente()
        print(f'Pago {id_pago} rechazado.')
    except PagoNoPendiente:
        print('El pago ya no está PENDIENTE. Pago NO modificado.')
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")