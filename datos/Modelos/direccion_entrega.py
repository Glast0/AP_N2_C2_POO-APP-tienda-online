from peewee import Model, AutoField, CharField, IntegerField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class DireccionEntrega(BaseModel):
    id_direccion_entrega = AutoField()
    id_cliente = IntegerField(index=True)
    calle = CharField(max_length=100)
    numero = CharField(max_length=15)
    comuna = CharField(max_length=50)
    ciudad = CharField(max_length=50)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'direccion_entregas'