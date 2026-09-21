class DetallePedido:
    def __init__(self,cantidad:int,producto:str):
        if cantidad <=0:
            raise ValueError("La cantidad debe ser mayor a 0.")   
        self.__cantidad=cantidad
        self.__producto=producto
        self.__precioUnitario = producto.precio