from datos.repositorios.repositorio_direcciones import (
    listado_direcciones, guardar_direccion, buscar_direccion, actualizar_direccion, direcciones_de_cliente)
from datos.repositorios.repositorio_clientes import buscar_cliente
from prettytable import PrettyTable
from datos.modelos.direccion_entrega import DireccionEntrega

def lista_direcciones():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Id cliente', 'Calle', 'Número', 'Comuna', 'Ciudad', 'Habilitado']

    direcciones = listado_direcciones()
    if direcciones:
        for d in direcciones:
            tabla.add_row([d.id_direccion_entrega, d.id_cliente, d.calle, d.numero,
                           d.comuna, d.ciudad, ('Deshabilitado', 'Habilitado')[d.habilitado]])
        print(tabla)

def crear_direccion(id_cliente, calle, numero, comuna, ciudad):
    # Regla de negocio: el cliente debe existir
    if buscar_cliente(id_cliente) is None:
        print(f'El cliente con Id {id_cliente} no existe. Dirección NO guardada.')
        return

    nueva = DireccionEntrega()
    nueva.id_cliente = id_cliente
    nueva.calle = calle
    nueva.numero = numero
    nueva.comuna = comuna
    nueva.ciudad = ciudad
    guardar_direccion(nueva)

def obtener_direccion(id_direccion):
    return buscar_direccion(id_direccion)

def modificar_direccion(id_direccion, calle, numero, comuna, ciudad):
    direccion = buscar_direccion(id_direccion)
    if direccion is None:
        print(f'La dirección con Id {id_direccion} no existe. Cambios NO guardados.')
        return
    if '' in (calle.strip(), numero.strip(), comuna.strip(), ciudad.strip()):
        print('Ningún campo puede quedar vacío. Cambios NO guardados.')
        return
    if (calle == direccion.calle and numero == direccion.numero
            and comuna == direccion.comuna and ciudad == direccion.ciudad):
        print('No hubo cambios. Nada que actualizar.')
        return

    direccion.calle = calle
    direccion.numero = numero
    direccion.comuna = comuna
    direccion.ciudad = ciudad
    actualizar_direccion(direccion)

def lista_direcciones_de_cliente(id_cliente):
    """Muestra las direcciones del cliente. Devuelve False si no tiene ninguna."""
    direcciones = list(direcciones_de_cliente(id_cliente))
    if not direcciones:
        return False

    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Calle', 'Número', 'Comuna', 'Ciudad', 'Habilitado']
    for d in direcciones:
        tabla.add_row([d.id_direccion_entrega, d.calle, d.numero, d.comuna,
                       d.ciudad, ('Deshabilitado', 'Habilitado')[d.habilitado]])
    print(tabla)
    return True

def direccion_es_del_cliente(id_direccion, id_cliente):
    direccion = buscar_direccion(id_direccion)
    return direccion is not None and direccion.id_cliente == id_cliente