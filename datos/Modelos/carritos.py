from peewee import *
from datos.conexion import conectar_db

database = conectar_db()

try:
    database.connect()
    print("¡Conexión exitosa!")
except OperationalError as e:
    print(f"Error detallado de conexión: {e}")

class BaseModel(Model):
    class Meta:
        database = database

class Carrito(BaseModel):
    id_carrito = AutoField()
    id_cliente = IntegerField(unique=True)
    fecha_creacion = DateField()
    habilitado = IntegerField(constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 'carritos'

