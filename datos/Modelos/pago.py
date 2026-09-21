from datetime import date

class Pago:
    def __init__(self,id:int,monto:float,,metodopago:str):
        self.__id=id
        self.__monto=monto
        self.__fecha=date.today()
        self.__metodopago=metodopago
        self.__estado = Estadopago. PENDIENTE


