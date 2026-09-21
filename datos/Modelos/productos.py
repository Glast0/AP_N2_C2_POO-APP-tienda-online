class Productos:
    def __init__(self,id:int,nombre:str,descripcion:str,precio:float,stockDisponible:int):
        self.__nombre=nombre
        self.__id=id
        self.__descripcion=descripcion
        self.__precio=precio
        self.__stockDisponible=stockDisponible

    def consultarDisponibilidad(self, cantidad:int =1) ->bool:
        return self.__stockDisponible >= cantidad

    def actualizarStock (self):
        return 