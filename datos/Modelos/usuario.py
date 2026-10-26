from peewee import Model, OperationalError
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class META:
        database=database
class Usuario(BaseModel):
    id_usuario
    rut 
    nombre
    apellido
    correo
    pais 
    fecha_nacimiento
    genero
    fecha_incorporacion
    habilitado
    password   