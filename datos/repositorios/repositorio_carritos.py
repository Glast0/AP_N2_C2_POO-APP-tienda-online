from datos.modelos.carritos import Carritos

def listado_carritos():
    carritos = Carritos.select()
    if carritos:
        return carritos