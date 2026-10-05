from peewee import DateField,IntegerField,AutoField,CharField,SQL,DecimalField,Model,DateTimeField,TextField
# pendiente from decouple import config
from datos.conexion import conectar_db
from auxiliares import defecto

defecto = 'DEFAULT 1'

database = conectar_db

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Carritos(BaseModel):
    fecha_creacion = DateField()
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_carrito = AutoField()
    id_cliente = IntegerField(unique=True)

    class Meta:
        table_name = 'carritos'

class Categorias(BaseModel):
    descripcion = CharField(max_length=150, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_categoria = AutoField()
    nombre_categoria = CharField(max_length=50)

    class Meta:
        table_name = 'categorias'

class Clientes(BaseModel):
    email = CharField(max_length=100, unique=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_cliente = AutoField()
    nombre = CharField(max_length=100)
    rut = CharField(max_length=12, unique=True)
    telefono = CharField(max_length=20, null=True)

    class Meta:
        table_name = 'clientes'

class DetallePedidos(BaseModel):
    cantidad = IntegerField()
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_detalle_pedido = AutoField()
    id_pedido = IntegerField(index=True)
    id_producto = IntegerField(index=True)
    precio_unitario = DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        table_name = 'detalle_pedidos'

class DireccionEntregas(BaseModel):
    calle = CharField(max_length=100)
    ciudad = CharField(max_length=50)
    comuna = CharField(max_length=50)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_cliente = IntegerField(index=True)
    id_direccion_entrega = AutoField()
    numero = CharField(max_length=15)

    class Meta:
        table_name = 'direccion_entregas'

class Envios(BaseModel):
    fecha_despacho = DateField(null=True)
    fecha_entrega_estimada = DateField(null=True)
    fecha_entrega_real = DateField(null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_envio = AutoField()
    id_pedido = IntegerField(unique=True)
    numero_seguimiento = CharField(max_length=100, null=True)
    transportista = CharField(max_length=50, null=True)

    class Meta:
        table_name = 'envios'

class EstadosPago(BaseModel):
    id_estado_pago = IntegerField(primary_key=True)
    nombre = CharField(max_length=20, unique=True)

    class Meta:
        table_name = 'estados_pago'

class EstadosPedido(BaseModel):
    id_estado_pedido = IntegerField(primary_key=True)
    nombre = CharField(max_length=20, unique=True)

    class Meta:
        table_name = 'estados_pedido'

class ItemCarritos(BaseModel):
    cantidad = IntegerField(constraints=[SQL(defecto)])
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_carrito = IntegerField(index=True)
    id_item_carrito = AutoField()
    id_producto = IntegerField(index=True)
    precio_unitario = DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        table_name = 'item_carritos'

class Pagos(BaseModel):
    fecha = DateTimeField()
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_estado_pago = IntegerField(constraints=[SQL(defecto)], index=True)
    id_pago = AutoField()
    id_pedido = IntegerField(index=True)
    metodo_pago = CharField(max_length=50)
    monto = DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        table_name = 'pagos'

class Pedidos(BaseModel):
    fecha = DateField()
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_cliente = IntegerField(index=True)
    id_direccion_entrega = IntegerField(index=True)
    id_estado_pedido = IntegerField(constraints=[SQL(defecto)], index=True)
    id_pedido = AutoField()
    total = DecimalField(constraints=[SQL("DEFAULT 0.00")], decimal_places=2, max_digits=10)

    class Meta:
        table_name = 'pedidos'

class Productos(BaseModel):
    descripcion = TextField(null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_categoria = IntegerField(index=True)
    id_producto = AutoField()
    nombre_producto = CharField(max_length=100)
    precio = DecimalField(decimal_places=2, max_digits=10)
    stock_disponible = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'productos'

