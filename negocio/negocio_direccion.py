from datos.repositorios.repositorio_direcciones import listado_direcciones, guardar_direccion
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