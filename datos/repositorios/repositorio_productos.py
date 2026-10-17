from datos.modelos.producto import Producto
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_productos():
    productos = Producto.select()
    if productos:
        return productos

def guardar_producto(producto: Producto):
    try:
        resultado = producto.save()
        if resultado == 1:
            print(f'Producto guardado con éxito con Id: {producto.id_producto}.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

def buscar_producto(id_producto: int):
    return Producto.get_or_none(Producto.id_producto == id_producto)

def actualizar_producto(producto: Producto):
    try:
        producto.save()
        print(f'Producto {producto.id_producto} actualizado con éxito.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron actualizar los datos por un error genérico: {e}")