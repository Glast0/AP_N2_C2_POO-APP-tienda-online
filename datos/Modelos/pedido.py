from peewee import Model, AutoField, IntegerField, DateField, DecimalField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Pedido(BaseModel):
    id_pedido = AutoField()
    fecha = DateField()
    total = DecimalField(max_digits=10, decimal_places=2, default=0)
    id_cliente = IntegerField(index=True)
    id_direccion_entrega = IntegerField(index=True)
    id_estado_pedido = IntegerField(default=1)  # 1 = CREADO
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'pedidos'

class DetallePedido(BaseModel):
    id_detalle_pedido = AutoField()
    id_pedido = IntegerField(index=True)
    id_producto = IntegerField(index=True)
    cantidad = IntegerField()
    precio_unitario = DecimalField(max_digits=10, decimal_places=2)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'detalle_pedidos'