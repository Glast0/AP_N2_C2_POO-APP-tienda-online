from datos.repositorios.repositorio_clientes import listado_clientes, guardar_cliente
from prettytable import PrettyTable
from datos.modelos.cliente import Cliente

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