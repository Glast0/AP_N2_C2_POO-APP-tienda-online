from datos.repositorios.repositorio_clientes import (
    listado_usuarios, guardar_usuarios)
from prettytable import PrettyTable
from datos.modelos.usuario import Usuario
from datetime import datetime
from auxiliares.mensajes import mensaje_error

def lista_usuarios(tabla_usuarios:PrettyTable):
    usuarios = listado_usuarios()
    tabla_usuarios.field_names = ['Id','RUT','Nombre Completo','Correo','Fecha Nacimiento']
    if usuarios:
        for usuario in usuarios:
            nombre_completo = f'{usuario.nombre} {usuario.apellido}'
            tabla_usuarios.add_row([usuario.id_usuario, usuario.rut, nombre_completo, usuario.correo, usuario.fecha_nacimiento])
        return tabla_usuarios

def crear_usuario(str_rut, str_nombre, str_apellido, str_correo, fecha_nacimiento, str_contrasenia):
    nuevo_usuario = Usuario()
    try:
        nuevo_usuario.rut = str_rut
        nuevo_usuario.nombre = str_nombre.title()
        nuevo_usuario.apellido = str_apellido.title()
        nuevo_usuario.correo = str_correo
        nuevo_usuario.fecha_nacimiento = fecha_nacimiento
        nuevo_usuario.password = str_contrasenia
        nuevo_usuario.fecha_incorporacion = datetime.now()
        nuevo_usuario.habilitado = True

        guardar_usuarios(nuevo_usuario)
    except Exception as error:
        print(f'{mensaje_error} {error}')