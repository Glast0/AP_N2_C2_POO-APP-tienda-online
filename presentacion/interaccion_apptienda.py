from datos.repositorios.repositorio_carritos import listado_carritos
from prettytable import PrettyTable

def lista_carritos():
    tabla_productos = PrettyTable()
    tabla_productos.field_names(["Nombre_campo1", "Nombre_campo2"])

    carritos = listado_carritos()
    if listado_carritos:
        for producto in carritos:
            tabla_productos.add_row([carritos.id_carrito, ...])
            print(f"tatata {carritos.id_carrito = } tatata")