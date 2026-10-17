from peewee import Model, OperationalError
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