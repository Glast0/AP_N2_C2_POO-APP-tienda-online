from datos.repositorios.repositorio_categorias import (
    listado_categorias, guardar_categoria, buscar_categoria, actualizar_categoria)
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

def obtener_categoria(id_categoria):
    return buscar_categoria(id_categoria)

def modificar_categoria(id_categoria, nombre, descripcion):
    categoria = buscar_categoria(id_categoria)
    if categoria is None:
        print(f'La categoría con Id {id_categoria} no existe. Cambios NO guardados.')
        return
    if nombre.strip() == '':
        print('El nombre no puede quedar vacío. Cambios NO guardados.')
        return
    if nombre == categoria.nombre_categoria and descripcion == categoria.descripcion:
        print('No hubo cambios. Nada que actualizar.')
        return

    categoria.nombre_categoria = nombre
    categoria.descripcion = descripcion
    actualizar_categoria(categoria)