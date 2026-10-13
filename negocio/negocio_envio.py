from datetime import date
from prettytable import PrettyTable
from datos.repositorios.repositorio_envios import (
    listado_envios, buscar_envio_de_pedido, guardar_envio)
from datos.repositorios.repositorio_pedidos import buscar_pedido
from datos.modelos.envio import Envio

def lista_envios():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Id pedido', 'Transportista', 'Seguimiento',
                         'Despacho', 'Entrega estimada', 'Entrega real']

    envios = listado_envios()
    if envios:
        for e in envios:
            tabla.add_row([e.id_envio, e.id_pedido, e.transportista, e.numero_seguimiento,
                           e.fecha_despacho, e.fecha_entrega_estimada, e.fecha_entrega_real])
        print(tabla)

def crear_envio(id_pedido, transportista, numero_seguimiento, fecha_estimada):
    # Reglas de negocio
    pedido = buscar_pedido(id_pedido)
    if pedido is None:
        print(f'El pedido con Id {id_pedido} no existe. Envío NO guardado.')
        return
    if pedido.id_estado_pedido == 6:  # CANCELADO
        print('El pedido está CANCELADO, no admite envío. Envío NO guardado.')
        return
    if buscar_envio_de_pedido(id_pedido) is not None:
        print(f'El pedido {id_pedido} ya tiene un envío registrado. Envío NO guardado.')
        return
    if fecha_estimada < date.today():
        print('La fecha de entrega estimada no puede ser anterior a hoy. Envío NO guardado.')
        return

    nuevo = Envio()
    nuevo.id_pedido = id_pedido
    nuevo.transportista = transportista
    nuevo.numero_seguimiento = numero_seguimiento
    nuevo.fecha_despacho = date.today()
    nuevo.fecha_entrega_estimada = fecha_estimada
    guardar_envio(nuevo)