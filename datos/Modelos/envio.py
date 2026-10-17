from peewee import AutoField, CharField, IntegerField, DateField
from datos.modelos.base import BaseModel

class Envio(BaseModel):
    id_envio = AutoField()
    id_pedido = IntegerField(unique=True)
    transportista = CharField(max_length=50, null=True)
    numero_seguimiento = CharField(max_length=100, null=True)
    fecha_despacho = DateField(null=True)
    fecha_entrega_estimada = DateField(null=True)
    fecha_entrega_real = DateField(null=True)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'envios'