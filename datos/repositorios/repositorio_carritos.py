from datos.modelos.carritos import Carrito, ItemCarrito
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_carritos():
    carritos = Carrito.select()
    if carritos:
        return carritos

def buscar_carrito(id_carrito: int):
    return Carrito.get_or_none(Carrito.id_carrito == id_carrito)

def buscar_carrito_de_cliente(id_cliente: int):
    return Carrito.get_or_none(Carrito.id_cliente == id_cliente)

def listado_items(id_carrito: int):
    return ItemCarrito.select().where(ItemCarrito.id_carrito == id_carrito)

def buscar_item_en_carrito(id_carrito: int, id_producto: int):
    return ItemCarrito.get_or_none(
        (ItemCarrito.id_carrito == id_carrito) & (ItemCarrito.id_producto == id_producto))

def guardar_carrito(carrito: Carrito):
    try:
        resultado = carrito.save()
        if resultado == 1:
            print(f'Carrito guardado con éxito con Id: {carrito.id_carrito}.')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea (¿el cliente ya tiene carrito?): {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

def guardar_item(item: ItemCarrito):
    try:
        resultado = item.save()
        if resultado == 1:
            print(f'Producto agregado al carrito (Id ítem: {item.id_item_carrito}).')
    except IntegrityError as e:
        print(f"Error de clave única o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional (conexión perdida, tabla inexistente o BD bloqueada): {e}")
    except DataError as e:
        print(f"El valor ingresado NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")