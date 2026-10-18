from datos.repositorios.repositorio_clientes import (
    listado_clientes, guardar_cliente, buscar_cliente, buscar_cliente_por_rut,
    buscar_cliente_por_email, actualizar_cliente, deshabilitar_cliente)
from datos.repositorios.repositorio_pedidos import pedidos_en_curso_de_cliente
from prettytable import PrettyTable
from datos.modelos.cliente import Cliente
from auxiliares.validaciones import rut_valido

def lista_clientes():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Nombre', 'RUT', 'Email', 'Teléfono', 'Habilitado']

    clientes = listado_clientes()
    if clientes:
        for c in clientes:
            tabla.add_row([c.id_cliente, c.nombre, c.rut, c.email, c.telefono,
                           ('Deshabilitado', 'Habilitado')[c.habilitado]])
        print(tabla)

def crear_cliente(nombre, rut, email, telefono):
    # Regla de negocio: validar antes de tocar la base de datos
    if '@' not in email or '.' not in email:
        print('El email ingresado no es válido. Cliente NO guardado.')
        return

    nuevo = Cliente()
    nuevo.nombre = nombre
    nuevo.rut = rut
    nuevo.email = email
    nuevo.telefono = telefono
    guardar_cliente(nuevo)

def obtener_cliente(id_cliente):
    return buscar_cliente(id_cliente)

def modificar_cliente(id_cliente, nombre, rut, email, telefono):
    cliente = buscar_cliente(id_cliente)
    if cliente is None:
        print(f'El cliente con Id {id_cliente} no existe. Cambios NO guardados.')
        return
    if nombre.strip() == '':
        print('El nombre no puede quedar vacío. Cambios NO guardados.')
        return

    # Solo se valida lo que cambió, para no rechazar datos antiguos que ya estaban en la BD
    if rut != cliente.rut:
        if not rut_valido(rut):
            print('El RUT ingresado no es válido. Cambios NO guardados.')
            return
        otro = buscar_cliente_por_rut(rut)
        if otro is not None and otro.id_cliente != id_cliente:
            print('Ese RUT ya pertenece a otro cliente. Cambios NO guardados.')
            return

    if email != cliente.email:
        if '@' not in email or '.' not in email:
            print('El email ingresado no es válido. Cambios NO guardados.')
            return
        otro = buscar_cliente_por_email(email)
        if otro is not None and otro.id_cliente != id_cliente:
            print('Ese email ya pertenece a otro cliente. Cambios NO guardados.')
            return

    if (nombre == cliente.nombre and rut == cliente.rut
            and email == cliente.email and telefono == cliente.telefono):
        print('No hubo cambios. Nada que actualizar.')
        return

    cliente.nombre = nombre
    cliente.rut = rut
    cliente.email = email
    cliente.telefono = telefono
    actualizar_cliente(cliente)

def eliminar_cliente(id_cliente):
    cliente = buscar_cliente(id_cliente)
    if cliente is None:
        print(f'El cliente con Id {id_cliente} no existe. Cliente NO eliminado.')
        return
    if cliente.habilitado == 0:
        print('El cliente ya está deshabilitado. Nada que hacer.')
        return
    if pedidos_en_curso_de_cliente(id_cliente).count() > 0:
        print('El cliente tiene pedidos en curso. Espere a que terminen o cancélelos. '
              'Cliente NO eliminado.')
        return

    deshabilitar_cliente(cliente)