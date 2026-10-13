import sys
from auxiliares import nombre_aplicacion,version_aplicacion,menu_superior,menu_apptienda
from presentacion.interaccion_apptienda import lista_carritos

from auxiliares import menu_categorias
from negocio.negocio_categoria import lista_categorias
from presentacion.presentacion_categorias import solicitar_datos_categoria

from auxiliares import menu_clientes
from negocio.negocio_cliente import lista_clientes
from presentacion.presentacion_clientes import solicitar_datos_cliente

from auxiliares import menu_productos
from negocio.negocio_productos import lista_productos
from presentacion.presentacion_productos import solicitar_datos_producto

from auxiliares import menu_direcciones
from negocio.negocio_direccion import lista_direcciones
from presentacion.presentacion_direcciones import solicitar_datos_direccion

from auxiliares import menu_pedidos
from negocio.negocio_pedido import lista_pedidos
from presentacion.presentacion_pedidos import solicitar_datos_pedido, solicitar_detalle_pedido

from auxiliares import menu_pagos
from negocio.negocio_pago import lista_pagos
from presentacion.presentacion_pagos import solicitar_datos_pago

from auxiliares import menu_envios
from negocio.negocio_envio import lista_envios
from presentacion.presentacion_envios import solicitar_datos_envio

from auxiliares import menu_carritos
from negocio.negocio_carritos import lista_carritos
from presentacion.presentacion_carritos import (
    solicitar_datos_carrito, solicitar_datos_item, solicitar_items_carrito)

def menu_principal():
    print(f'\n{nombre_aplicacion} - {version_aplicacion}')
    print(f'{'=' * len(nombre_aplicacion)}==={'=' * len(version_aplicacion)}\n')

    while True:
        for clave,valor in menu_superior.items():
            print(f'[{clave}] - {valor}')
        opcion_usuario = input('\nIngrese su opción [1-9]: ')

        if opcion_usuario == '1':
            for numero,nombre in menu_apptienda.items():
                print(f'[{numero}] - {nombre}')

            opcion_sub_menu = input('\nIngrese su opción [0-2]: ')
            if opcion_sub_menu == '1':  
                lista_carritos()

        elif opcion_usuario == '2':
            for numero, nombre in menu_categorias.items():
                print(f'[{numero}] - {nombre}')

            opcion_sub_menu = input('\nIngrese su opción [0-2]: ')
            
            if opcion_sub_menu == '1':
                lista_categorias()

            elif opcion_sub_menu == '2':
                solicitar_datos_categoria()

        elif opcion_usuario == '3':
            for numero, nombre in menu_clientes.items():
                print(f'[{numero}] - {nombre}')
        
            opcion_sub_menu = input('\nIngrese su opción [0-2]: ')
            if opcion_sub_menu == '1':
                lista_clientes()
            elif opcion_sub_menu == '2':
                solicitar_datos_cliente()

        elif opcion_usuario == '4':
            for numero, nombre in menu_productos.items():
                print(f'[{numero}] - {nombre}')

            opcion_sub_menu = input('\nIngrese su opción [0-2]: ')
            if opcion_sub_menu == '1':
                lista_productos()
            elif opcion_sub_menu == '2':
                solicitar_datos_producto()

        elif opcion_usuario == '5':
            for numero, nombre in menu_direcciones.items():
                print(f'[{numero}] - {nombre}')

            opcion_sub_menu = input('\nIngrese su opción [0-2]: ')
            if opcion_sub_menu == '1':
                lista_direcciones()
            elif opcion_sub_menu == '2':
                solicitar_datos_direccion()

        elif opcion_usuario == '6':
            for numero, nombre in menu_pedidos.items():
                print(f'[{numero}] - {nombre}')

            opcion_sub_menu = input('\nIngrese su opción [0-3]: ')
            if opcion_sub_menu == '1':
                lista_pedidos()
            elif opcion_sub_menu == '2':
                solicitar_datos_pedido()
            elif opcion_sub_menu == '3':
                solicitar_detalle_pedido()

        elif opcion_usuario == '7':
            for numero, nombre in menu_pagos.items():
                print(f'[{numero}] - {nombre}')

            opcion_sub_menu = input('\nIngrese su opción [0-2]: ')
            if opcion_sub_menu == '1':
                lista_pagos()
            elif opcion_sub_menu == '2':
                solicitar_datos_pago()

        elif opcion_usuario == '8':
            for numero, nombre in menu_envios.items():
                print(f'[{numero}] - {nombre}')
        
            opcion_sub_menu = input('\nIngrese su opción [0-2]: ')
            if opcion_sub_menu == '1':
                lista_envios()
            elif opcion_sub_menu == '2':
                solicitar_datos_envio()

        elif opcion_usuario == '9':
            for numero, nombre in menu_carritos.items():
                print(f'[{numero}] - {nombre}')
        
            opcion_sub_menu = input('\nIngrese su opción [0-4]: ')
            if opcion_sub_menu == '1':
                lista_carritos()
            elif opcion_sub_menu == '2':
                solicitar_datos_carrito()
            elif opcion_sub_menu == '3':
                solicitar_datos_item()
            elif opcion_sub_menu == '4':
                solicitar_items_carrito()

        elif opcion_usuario == '0':
            print('Saliendo...')
            sys.exit()

        else:
            print('Opción ingresada NO corresponde...\nIngrese nuevamente')

menu_principal()