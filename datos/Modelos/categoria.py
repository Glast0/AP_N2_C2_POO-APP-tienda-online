
class Categorias:
    def __init__(self,id : int,nombre : str,descripcion : str):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__productos = []

    def list_productos(self):
        return self.__productos

    


