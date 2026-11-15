from getpass import getpass

from negocio.negocio_usuario import (
    lista_usuarios, crear_usuario, obtener_usuario, modificar_usuario, eliminar_usuario)
from presentacion.presentacion_pedidos import pedir_entero
from auxiliares.validaciones import rut_valido, correo_valido, fecha_nacimiento_valida, errores_contrasenia

def solicitar_datos_usuario():
    rut = nombre = apellido = correo = password = ''
    fecha_nacimiento = None

    print('\n--- Crear usuario ---')
    while rut == '':
        rut = input('Ingrese RUT (ej: 12.345.678-5): ').strip()
        if not rut_valido(rut):
            print('RUT inválido, ingrese nuevamente...')
            rut = ''

    while nombre == '':
        nombre = input('Ingrese nombre: ').strip()
    while apellido == '':
        apellido = input('Ingrese apellido: ').strip()

    while correo == '':
        correo = input('Ingrese correo: ').strip()
        if not correo_valido(correo):
            print('Correo NO válido, ingrese nuevamente...')
            correo = ''

    while fecha_nacimiento is None:
        fecha_nacimiento = fecha_nacimiento_valida(input('Fecha de nacimiento (dd/mm/yyyy): ').strip())
        if fecha_nacimiento is None:
            print('Fecha inválida, ingrese nuevamente...')

    while password == '':
        password = getpass('Ingrese contraseña: ')
        errores = errores_contrasenia(password)
        if errores:
            print('Contraseña inválida, revise lo siguiente:')
            for e in errores:
                print(f' - {e}')
            password = ''
            continue
        if getpass('Repita la contraseña: ') != password:
            print('Las contraseñas no coinciden.')
            password = ''

    crear_usuario(rut, nombre, apellido, correo, fecha_nacimiento, password)

def solicitar_modificacion_usuario():
    print('\nUsuarios disponibles:')
    lista_usuarios()

    usuario = None
    while usuario is None:
        id_usuario = pedir_entero('Ingrese el Id del usuario a modificar (0 para cancelar): ')
        if id_usuario == 0:
            print('Modificación cancelada.')
            return
        usuario = obtener_usuario(id_usuario)
        if usuario is None:
            print(f'El usuario con Id {id_usuario} no existe. Intente nuevamente.')

    print(f'\nNombre actual: {usuario.nombre}')
    nombre = input('Nuevo nombre (Enter para mantener): ')
    if nombre == '':
        nombre = usuario.nombre

    print(f'Apellido actual: {usuario.apellido}')
    apellido = input('Nuevo apellido (Enter para mantener): ')
    if apellido == '':
        apellido = usuario.apellido

    print(f'Correo actual: {usuario.correo}')
    correo = input('Nuevo correo (Enter para mantener): ')
    if correo == '':
        correo = usuario.correo

    print(f'Fecha de nacimiento actual: {usuario.fecha_nacimiento}')
    fecha_nacimiento = None
    while fecha_nacimiento is None:
        texto = input('Nueva fecha dd/mm/yyyy (Enter para mantener): ').strip()
        if texto == '':
            fecha_nacimiento = usuario.fecha_nacimiento
            break
        fecha_nacimiento = fecha_nacimiento_valida(texto)
        if fecha_nacimiento is None:
            print('Fecha inválida, ingrese nuevamente...')

    modificar_usuario(usuario.id_usuario, nombre, apellido, correo, fecha_nacimiento)

def solicitar_eliminacion_usuario():
    print('\nUsuarios disponibles:')
    lista_usuarios()

    usuario = None
    while usuario is None:
        id_usuario = pedir_entero('Ingrese el Id del usuario a eliminar (0 para cancelar): ')
        if id_usuario == 0:
            print('Eliminación cancelada.')
            return
        usuario = obtener_usuario(id_usuario)
        if usuario is None:
            print(f'El usuario con Id {id_usuario} no existe. Intente nuevamente.')

    confirmar = input(f'¿Eliminar al usuario "{usuario.nombre} {usuario.apellido}"? [s/n]: ').strip().lower()
    if confirmar != 's':
        print('Eliminación cancelada.')
        return
    eliminar_usuario(usuario.id_usuario)