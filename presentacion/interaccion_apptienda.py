from datos.repositorios.repositorio_carritos import listado_carritos
from prettytable import PrettyTable

def lista_carritos():
    # Instancia de la clase PrettyTable
    tabla_carritos = PrettyTable()
    tabla_carritos.field_names = ['ID Carrito', 'ID Cliente', 'Fecha Creación', 'Habilitado']

    carritos = listado_carritos()
    if carritos:
        for carrito in carritos:
            tabla_carritos.add_row([
                carrito.id_carrito, 
                carrito.id_cliente, 
                carrito.fecha_creacion, 
                carrito.habilitado
            ])
        print(tabla_carritos)