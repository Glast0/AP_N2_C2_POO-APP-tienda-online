from peewee import Model, AutoField, CharField, TextField, IntegerField, DecimalField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Producto(BaseModel):
    id_producto = AutoField()
    nombre_producto = CharField(max_length=100)
    descripcion = TextField(null=True)
    precio = DecimalField(max_digits=10, decimal_places=2)
    stock_disponible = IntegerField(default=0)
    id_categoria = IntegerField(index=True)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'productos'