import sys
from  auxiliares import nombre_aplicacion,version_aplicacion,menu_superior


def menu_principal():
    print(f'\n{nombre_aplicacion} - {version_aplicacion}')
    print(f'{'='*len(nombre_aplicacion)}==={'=' * len(version_aplicacion)}\n)')

    while True:
        for clave,valor in menu_superior.items():
            print(f'[{clave}] - {valor}')
        opcion_usuario=input('\nIngrese su opcion [1-4]:')

        if opcion_usuario == '1':
            print('Opcion 1')

        elif opcion_usuario == '2':
            print('Opcion 2')

        elif opcion_usuario == '3':
            print('Opcion 3')

        elif opcion_usuario == '0':
            print('Saliendo...')
            sys.exit()
        else:
            print('Opcion ingresada NO corresponde... \nIngrese nuevamente')



