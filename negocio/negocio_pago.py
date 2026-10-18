from datetime import datetime
from decimal import Decimal
from prettytable import PrettyTable
from datos.repositorios.repositorio_pagos import (
    listado_pagos, pagos_de_pedido, guardar_pago, buscar_pago, aprobar_pago_en_bd)
from datos.repositorios.repositorio_pedidos import buscar_pedido
from datos.modelos.pago import Pago

ESTADOS_PAGO = {1: 'PENDIENTE', 2: 'APROBADO', 3: 'RECHAZADO', 4: 'REEMBOLSADO'}
METODOS_PAGO = ['EFECTIVO', 'TARJETA_DEBITO', 'TARJETA_CREDITO', 'TRANSFERENCIA']

def lista_pagos():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Id pedido', 'Fecha', 'Monto', 'Método', 'Estado']

    pagos = listado_pagos()
    if pagos:
        for p in pagos:
            tabla.add_row([p.id_pago, p.id_pedido, p.fecha, p.monto, p.metodo_pago,
                           ESTADOS_PAGO.get(p.id_estado_pago, p.id_estado_pago)])
        print(tabla)

def crear_pago(id_pedido, monto, metodo_pago):
    # Reglas de negocio
    pedido = buscar_pedido(id_pedido)
    if pedido is None:
        print(f'El pedido con Id {id_pedido} no existe. Pago NO guardado.')
        return
    if pedido.id_estado_pedido == 6:  # CANCELADO
        print('El pedido está CANCELADO, no admite pagos. Pago NO guardado.')
        return
    if metodo_pago not in METODOS_PAGO:
        print('Método de pago no válido. Pago NO guardado.')
        return
    if not monto.is_finite() or monto <= 0:
        print('El monto debe ser un número mayor a 0. Pago NO guardado.')
        return

    # El monto no puede superar lo que falta por pagar
    # (se descuentan los pagos PENDIENTES y APROBADOS; los rechazados/reembolsados no cuentan)
    ya_pagado = sum((p.monto for p in pagos_de_pedido(id_pedido)
                     if p.id_estado_pago in (1, 2)), Decimal('0'))
    saldo = pedido.total - ya_pagado
    if monto > saldo:
        print(f'El monto supera el saldo pendiente del pedido ({saldo}). Pago NO guardado.')
        return

    nuevo = Pago()
    nuevo.id_pedido = id_pedido
    nuevo.fecha = datetime.now()
    nuevo.monto = monto
    nuevo.metodo_pago = metodo_pago
    guardar_pago(nuevo)

def obtener_pago(id_pago):
    return buscar_pago(id_pago)

def aprobar_pago(id_pago):
    pago = buscar_pago(id_pago)
    if pago is None:
        print(f'El pago con Id {id_pago} no existe. Pago NO modificado.')
        return
    if pago.id_estado_pago != 1:
        estado = ESTADOS_PAGO.get(pago.id_estado_pago, pago.id_estado_pago)
        print(f'El pago está {estado}; solo se pueden aprobar pagos PENDIENTES. Pago NO modificado.')
        return

    pedido = buscar_pedido(pago.id_pedido)
    if pedido is None:
        print(f'El pedido {pago.id_pedido} de este pago no existe. Pago NO modificado.')
        return
    if pedido.id_estado_pedido == 6:  # CANCELADO
        print('El pedido está CANCELADO, no se pueden aprobar sus pagos. Pago NO modificado.')
        return

    aprobar_pago_en_bd(id_pago, pago.id_pedido)