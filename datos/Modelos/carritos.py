from peewee import AutoField, IntegerField, DateField, DecimalField, OperationalError
from datos.modelos.base import BaseModel

class Carrito(BaseModel):
    id_carrito = AutoField()
    id_cliente = IntegerField(unique=True)
    fecha_creacion = DateField()
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'carritos'

class ItemCarrito(BaseModel):
    id_item_carrito = AutoField()
    id_carrito = IntegerField(index=True)
    id_producto = IntegerField(index=True)
    cantidad = IntegerField(default=1)
    precio_unitario = DecimalField(max_digits=10, decimal_places=2)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'item_carritos'