from datos.modelos.cliente import Cliente
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_clientes():
    clientes = Cliente.select()
    if clientes:
        return clientes

def guardar_cliente(cliente: Cliente):
    try:
        resultado = cliente.save()
        if resultado == 1:
            print(f'Cliente guardado con éxito con Id: {cliente.id_cliente}.')
    except IntegrityError as e:
        print(f"Error: el RUT o el email ya existen, o hay una clave foránea inválida: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

def buscar_cliente(id_cliente: int):
    return Cliente.get_or_none(Cliente.id_cliente == id_cliente)

def buscar_cliente_por_rut(rut: str):
    return Cliente.get_or_none(Cliente.rut == rut)

def buscar_cliente_por_email(email: str):
    return Cliente.get_or_none(Cliente.email == email)

def actualizar_cliente(cliente: Cliente):
    try:
        cliente.save()
        print(f'Cliente {cliente.id_cliente} actualizado con éxito.')
    except IntegrityError as e:
        print(f"Error: el RUT o el email ya existen, o hay una clave foránea inválida: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")

def deshabilitar_cliente(cliente: Cliente):
    try:
        cliente.habilitado = 0
        cliente.save()
        print(f'Cliente {cliente.id_cliente} eliminado con éxito.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudo eliminar por un error genérico: {e}")