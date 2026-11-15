from peewee import AutoField, CharField, IntegerField, DateField
from datos.modelos.base import BaseModel

class Usuario(BaseModel):
    id_usuario = AutoField()
    rut = CharField(max_length=12, unique=True)
    nombre = CharField(max_length=25)
    apellido = CharField(max_length=25)
    correo = CharField(max_length=255, unique=True)
    fecha_nacimiento = DateField(null=True)
    fecha_incorporacion = DateField()
    habilitado = IntegerField(default=1)
    password = CharField(max_length=60)

    class Meta:
        table_name = 'usuarios'