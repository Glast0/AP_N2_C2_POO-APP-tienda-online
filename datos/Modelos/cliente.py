from peewee import Model, AutoField, CharField, IntegerField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Cliente(BaseModel):
    id_cliente = AutoField()
    nombre = CharField(max_length=100)
    rut = CharField(max_length=12, unique=True)
    email = CharField(max_length=100, unique=True)
    telefono = CharField(max_length=20, null=True)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'clientes'