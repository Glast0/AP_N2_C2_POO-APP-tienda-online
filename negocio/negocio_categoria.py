from datos.repositorios.repositorio_categorias import listado_categorias, guardar_categoria
from prettytable import PrettyTable
from datos.modelos.categoria import Categoria

def lista_categorias():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'Categoría', 'Descripción', 'Habilitado']

    categorias = listado_categorias()
    if categorias:
        for c in categorias:
            tabla.add_row([c.id_categoria, c.nombre_categoria, c.descripcion,
                           ('Deshabilitado', 'Habilitado')[c.habilitado]])
        print(tabla)

def crear_categoria(nombre_categoria, descripcion):
    nueva = Categoria()
    nueva.nombre_categoria = nombre_categoria
    nueva.descripcion = descripcion
    guardar_categoria(nueva)