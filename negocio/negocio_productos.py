from datos.repositorios.repositorio_productos import listado_productos, guardar_producto
from datos.repositorios.repositorio_categorias import buscar_categoria
from prettytable import PrettyTable
from datos.modelos.producto import Producto

def lista_productos():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Producto', 'Descripción', 'Precio', 'Stock', 'Id categoría', 'Habilitado']

    productos = listado_productos()
    if productos:
        for p in productos:
            tabla.add_row([p.id_producto, p.nombre_producto, p.descripcion, p.precio,
                           p.stock_disponible, p.id_categoria,
                           ('Deshabilitado', 'Habilitado')[p.habilitado]])
        print(tabla)

def crear_producto(nombre_producto, descripcion, precio, stock, id_categoria):
    # Reglas de negocio
    if not precio.is_finite():
        print('El precio ingresado no es válido. Producto NO guardado.')
        return
    if precio > 99999999.99:
        print('El precio supera el máximo permitido (99.999.999,99). Producto NO guardado.')
        return
    if stock > 1000000:
        print('El stock supera el máximo permitido (1.000.000). Producto NO guardado.')
        return
    if precio <= 0:
        print('El precio debe ser mayor a 0. Producto NO guardado.')
        return
    if stock < 0:
        print('El stock no puede ser negativo. Producto NO guardado.')
        return
    if buscar_categoria(id_categoria) is None:
        print(f'La categoría con Id {id_categoria} no existe. Producto NO guardado.')
        return

    nuevo = Producto()
    nuevo.nombre_producto = nombre_producto
    nuevo.descripcion = descripcion
    nuevo.precio = precio
    nuevo.stock_disponible = stock
    nuevo.id_categoria = id_categoria
    guardar_producto(nuevo)