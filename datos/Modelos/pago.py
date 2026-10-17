from peewee import AutoField, CharField, IntegerField, DecimalField, DateTimeField
from datos.modelos.base import BaseModel

class Pago(BaseModel):
    id_pago = AutoField()
    id_pedido = IntegerField(index=True)
    fecha = DateTimeField()
    monto = DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = CharField(max_length=50)
    id_estado_pago = IntegerField(default=1)  # 1 = PENDIENTE
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'pagos'