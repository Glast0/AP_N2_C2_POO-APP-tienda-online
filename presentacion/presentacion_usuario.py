from prettytable import PrettyTable
import re
from datetime import datetime
from negocio.negocio_usuario import lista_usuarios,crear_usuario,actualizar_usuario
from datos.modelos.usuario import Usuario



def mostrar_usuario():
    try:
        tabla_usuarios = PrettyTable()
        tabla_usuarios = lista_usuarios(tabla_usuarios)
        print(tabla_usuarios)
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')