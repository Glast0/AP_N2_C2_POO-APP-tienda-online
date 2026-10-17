from peewee import AutoField, CharField, IntegerField
from datos.modelos.base import BaseModel

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre_categoria = CharField(max_length=50)
    descripcion = CharField(max_length=150, null=True)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'categorias'