class DireccionEntrega:
    def __init__(self,id:int,calle:str,numero:str,ciudad:str,comuna:str):
        self.__id = id
        self.__calle = calle 
        self.__numero = numero
        self.__ciudad = ciudad
        self.__comuna = comuna

    def actualizarDireccion(self):
        return 