from datos.modelos.usuario import Usuario
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_usuarios():
    usuario = usuario.select()
    if usuario:
        return usuario

def guardar_usuario(usuario: Usuario):
    try:
        resultado = usuario.save()
        if resultado == 1:
            print(f'usuario guardado con éxito con Id: {usuario.id_usuario}.')
    except IntegrityError as e:
        print(f"Error: el RUT o el email ya existen, o hay una clave foránea inválida: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

def buscar_usuario(id_usuario: int):
    return Usuario.get_or_none(Usuario.id_usuario == id_usuario)

def buscar_usuario_por_rut(rut: str):
    return Usuario.get_or_none(Usuario.rut == rut)

def buscar_usuario_por_email(email: str):
    return Usuario.get_or_none(Usuario.email == email)

def actualizar_usuario(usuario: Usuario):
    try:
        usuario.save()
        print(f'usuario {usuario.id_usuario} actualizado con éxito.')
    except IntegrityError as e:
        print(f"Error: el RUT o el email ya existen, o hay una clave foránea inválida: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")

def deshabilitar_usuario(usuario: Usuario):
    try:
        usuario.habilitado = 0
        usuario.save()
        print(f'usuario {usuario.id_usuario} eliminado con éxito.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudo eliminar por un error genérico: {e}")