from peewee import *

class Carritos():
    fecha_creacion = DateField
    id_carrito = AutoField()
    id_cliente = IntegerField()
    habilitado = IntegerField(constraints=[SQL("DEFAULT 1")])
