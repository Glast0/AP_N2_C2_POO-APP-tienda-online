from datos.modelos.carritos import Carrito
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_carritos():
    carritos = Carrito.select()
    if carritos:
        return carritos

def guardar_carrito(carrito):
    try:
        carrito.save()
        if guardar_carrito == 1:
            print(f"Carrito guardado con éxito con id: {carrito.id_carrito}")
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (pérdida de conexión, falta una tabla, o base de datos bloqueada): {e}")
    except DataError as e:
        print(f"Valor insertado no corresponde")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")
