import sys
from auxiliares import nombre_aplicacion,version_aplicacion,menu_superior
from presentacion.interaccion_apptienda import lista_carritos

def menu_principal():
    print(f"{nombre_aplicacion} - {version_aplicacion}")
    print(f"{'=' * len(nombre_aplicacion)} === {'=' * len(version_aplicacion)}")
    print("App tienda")
    print("=========\n")
    while True:
        opcion_usuario = input("\nIngrese su opción [1-4]:")

        if opcion_usuario == "1":
            lista_carritos()
            pass
        elif opcion_usuario == "2":
            pass
        elif opcion_usuario == "3":
            pass
        elif opcion_usuario == "4":
            print("Saliendo...")
            sys.exit()
        else:
            print("La opción ingresada no es válida.")

menu_principal()