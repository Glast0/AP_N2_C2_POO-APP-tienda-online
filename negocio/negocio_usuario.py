from datetime import date
from prettytable import PrettyTable

from datos.modelos.usuario import Usuario
from datos.repositorios.repositorio_usuarios import (
    listado_usuarios, guardar_usuario, buscar_usuario, buscar_usuario_por_rut,
    buscar_usuario_por_correo, actualizar_usuario, deshabilitar_usuario)
from auxiliares.validaciones import rut_valido, formatear_rut, correo_valido, errores_contrasenia

def lista_usuarios():
    tabla = PrettyTable()
    tabla.field_names = ['Id', 'RUT', 'Nombre Completo', 'Correo', 'Fecha Nacimiento', 'Estado']

    usuarios = listado_usuarios()
    if usuarios:
        for u in usuarios:
            tabla.add_row([u.id_usuario, u.rut, f'{u.nombre} {u.apellido}', u.correo,
                           u.fecha_nacimiento, ('Deshabilitado', 'Habilitado')[u.habilitado]])
        print(tabla)

def obtener_usuario(id_usuario):
    return buscar_usuario(id_usuario)

def crear_usuario(rut, nombre, apellido, correo, fecha_nacimiento, password):
    # Regla de negocio: validar antes de tocar la base de datos
    if not rut_valido(rut):
        print('El RUT ingresado no es válido. Usuario NO guardado.')
        return
    rut = formatear_rut(rut)
    if buscar_usuario_por_rut(rut) is not None:
        print('Ya existe un usuario con ese RUT. Usuario NO guardado.')
        return

    correo = correo.strip().lower()
    if not correo_valido(correo):
        print('El correo ingresado no es válido. Usuario NO guardado.')
        return
    if buscar_usuario_por_correo(correo) is not None:
        print('Ya existe un usuario con ese correo. Usuario NO guardado.')
        return

    if nombre.strip() == '' or apellido.strip() == '':
        print('Nombre y apellido son obligatorios. Usuario NO guardado.')
        return

    errores = errores_contrasenia(password)
    if errores:
        print('Contraseña inválida:')
        for e in errores:
            print(f' - {e}')
        return

    nuevo = Usuario()
    nuevo.rut = rut
    nuevo.nombre = nombre.strip().title()
    nuevo.apellido = apellido.strip().title()
    nuevo.correo = correo
    nuevo.fecha_nacimiento = fecha_nacimiento
    nuevo.fecha_incorporacion = date.today()
    nuevo.habilitado = 1
    nuevo.password = password
    guardar_usuario(nuevo)

def modificar_usuario(id_usuario, nombre, apellido, correo, fecha_nacimiento):
    usuario = buscar_usuario(id_usuario)
    if usuario is None:
        print(f'El usuario con Id {id_usuario} no existe. Cambios NO guardados.')
        return
    if nombre.strip() == '' or apellido.strip() == '':
        print('Nombre y apellido no pueden quedar vacíos. Cambios NO guardados.')
        return

    correo = correo.strip().lower()
    if correo != usuario.correo:
        if not correo_valido(correo):
            print('El correo ingresado no es válido. Cambios NO guardados.')
            return
        otro = buscar_usuario_por_correo(correo)
        if otro is not None and otro.id_usuario != id_usuario:
            print('Ese correo ya pertenece a otro usuario. Cambios NO guardados.')
            return

    nombre = nombre.strip().title()
    apellido = apellido.strip().title()
    if (nombre == usuario.nombre and apellido == usuario.apellido
            and correo == usuario.correo and fecha_nacimiento == usuario.fecha_nacimiento):
        print('No hubo cambios. Nada que actualizar.')
        return

    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.correo = correo
    usuario.fecha_nacimiento = fecha_nacimiento
    actualizar_usuario(usuario)

def eliminar_usuario(id_usuario):
    usuario = buscar_usuario(id_usuario)
    if usuario is None:
        print(f'El usuario con Id {id_usuario} no existe. Usuario NO eliminado.')
        return
    if usuario.habilitado == 0:
        print('El usuario ya está deshabilitado. Nada que hacer.')
        return
    deshabilitar_usuario(usuario)