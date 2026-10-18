from datos.modelos.categoria import Categoria
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_categorias():
    categorias = Categoria.select()
    if categorias:
        return categorias

def guardar_categoria(categoria: Categoria):
    try:
        resultado = categoria.save()
        if resultado == 1:
            print(f'Categoría guardada con éxito con Id: {categoria.id_categoria}.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

def buscar_categoria(id_categoria: int):
    return Categoria.get_or_none(Categoria.id_categoria == id_categoria)

def actualizar_categoria(categoria: Categoria):
    try:
        categoria.save()
        print(f'Categoría {categoria.id_categoria} actualizada con éxito.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")

def deshabilitar_categoria(categoria: Categoria):
    try:
        categoria.habilitado = 0
        categoria.save()
        print(f'Categoría {categoria.id_categoria} eliminada con éxito.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudo eliminar por un error genérico: {e}")