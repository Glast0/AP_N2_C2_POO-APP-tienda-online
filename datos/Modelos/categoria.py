from peewee import Model, AutoField, CharField, IntegerField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre_categoria = CharField(max_length=50)
    descripcion = CharField(max_length=150, null=True)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'categorias'