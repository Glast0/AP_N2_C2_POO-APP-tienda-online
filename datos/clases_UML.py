
from __future__ import annotations
from enum import Enum
from datetime import date, timedelta
from typing import Optional

# =========================================================
# ENUMERACIONES
# =========================================================

class EstadoPedido(Enum):
    CREADO = "CREADO"
    CONFIRMADO = "CONFIRMADO"
    EN_PREPARACION = "EN_PREPARACION"
    ENVIADO = "ENVIADO"
    ENTREGADO = "ENTREGADO"
    CANCELADO = "CANCELADO"

class EstadoPago(Enum):
    PENDIENTE = "PENDIENTE"
    APROBADO = "APROBADO"
    RECHAZADO = "RECHAZADO"
    REEMBOLSADO = "REEMBOLSADO"

class Categoria:
    def __init__(self, id: int, nombre: str, descripcion: str = ""):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._productos: list["Producto"] = []  # lado "0..*" de la agregación

    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("El nombre de la categoría no puede estar vacío.")
        self._nombre = valor

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        self._descripcion = valor

    def _registrar_producto(self, producto: "Producto") -> None:
        """Uso interno: Producto la llama al asignarse esta categoría."""
        if producto not in self._productos:
            self._productos.append(producto)

    def listar_productos(self) -> list["Producto"]:
        return list(self._productos)

    def __repr__(self) -> str:
        return f"Categoria({self._nombre})"


class DireccionEntrega:
    def __init__(self, id: int, calle: str, numero: str, comuna: str, ciudad: str):
        self._id = id
        self._calle = calle
        self._numero = numero
        self._comuna = comuna
        self._ciudad = ciudad
        self._habilitada = True

    @property
    def id(self) -> int:
        return self._id

    @property
    def calle(self) -> str:
        return self._calle

    @calle.setter
    def calle(self, valor: str) -> None:
        self._calle = valor

    @property
    def numero(self) -> str:
        return self._numero

    @numero.setter
    def numero(self, valor: str) -> None:
        self._numero = valor

    @property
    def comuna(self) -> str:
        return self._comuna

    @comuna.setter
    def comuna(self, valor: str) -> None:
        self._comuna = valor

    @property
    def ciudad(self) -> str:
        return self._ciudad

    @ciudad.setter
    def ciudad(self, valor: str) -> None:
        self._ciudad = valor

    @property
    def habilitada(self) -> bool:
        return self._habilitada

    def actualizar_direccion(self, calle: str = None, numero: str = None,
                              comuna: str = None, ciudad: str = None) -> None:
        if not self._habilitada:
            raise ValueError("No se puede editar una dirección eliminada.")
        if calle is not None:
            self.calle = calle
        if numero is not None:
            self.numero = numero
        if comuna is not None:
            self.comuna = comuna
        if ciudad is not None:
            self.ciudad = ciudad

    def eliminar_direccion(self) -> None:
        self._habilitada = False

    def __repr__(self) -> str:
        estado = "" if self._habilitada else " [eliminada]"
        return f"{self._calle} {self._numero}, {self._comuna}, {self._ciudad}{estado}"

class Producto:
    def __init__(self, id: int, nombre: str, descripcion: str, precio: float,
                 stock_disponible: int, categoria: Optional[Categoria] = None):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock_disponible = stock_disponible
        self._categoria: Optional[Categoria] = None
        if categoria is not None:
            self.asignar_categoria(categoria)

    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self._nombre = valor

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        self._descripcion = valor

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    @property
    def stock_disponible(self) -> int:
        return self._stock_disponible  # sin setter: solo se cambia vía actualizar_stock()

    @property
    def categoria(self) -> Optional[Categoria]:
        return self._categoria

    def asignar_categoria(self, categoria: Categoria) -> None:
        """Materializa la agregación Categoria '1' o-- '0..*' Producto."""
        self._categoria = categoria
        categoria._registrar_producto(self)

    def consultar_disponibilidad(self, cantidad: int = 1) -> bool:
        return self._stock_disponible >= cantidad

    def actualizar_stock(self, cantidad: int) -> None:
        """cantidad negativa = salida (venta), positiva = entrada (reposición)."""
        nuevo_stock = self._stock_disponible + cantidad
        if nuevo_stock < 0:
            raise ValueError(f"Stock insuficiente para '{self._nombre}'.")
        self._stock_disponible = nuevo_stock

    def __repr__(self) -> str:
        return f"Producto({self._nombre}, ${self._precio})"

class ItemCarrito:
    """Clase de asociación: CarritoDeCompra <-> Producto."""

    def __init__(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        self._producto = producto
        self._cantidad = cantidad
        self._precio_unitario = producto.precio  # se congela al momento de agregar

    @property
    def producto(self) -> Producto:
        return self._producto

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        if valor <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        self._cantidad = valor

    @property
    def precio_unitario(self) -> float:
        return self._precio_unitario

    def calcular_subtotal(self) -> float:
        return self._cantidad * self._precio_unitario

    def __repr__(self) -> str:
        return f"ItemCarrito({self._cantidad}x {self._producto.nombre})"

class DetallePedido:
    """Clase de asociación: Pedido <-> Producto (línea de venta ya confirmada)."""

    def __init__(self, producto: Producto, cantidad: int, precio_unitario: float):
        self._producto = producto
        self._cantidad = cantidad
        self._precio_unitario = precio_unitario  # precio al momento de la compra

    @property
    def producto(self) -> Producto:
        return self._producto

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def precio_unitario(self) -> float:
        return self._precio_unitario

    def calcular_subtotal(self) -> float:
        return self._cantidad * self._precio_unitario

    def __repr__(self) -> str:
        return f"DetallePedido({self._cantidad}x {self._producto.nombre})"

class Pago:
    def __init__(self, id: int, monto: float, metodo_pago: str):
        self._id = id
        self._monto = monto
        self._fecha = date.today()
        self._metodo_pago = metodo_pago
        self._estado = EstadoPago.PENDIENTE

    @property
    def id(self) -> int:
        return self._id

    @property
    def monto(self) -> float:
        return self._monto

    @property
    def fecha(self) -> date:
        return self._fecha

    @property
    def metodo_pago(self) -> str:
        return self._metodo_pago

    @property
    def estado(self) -> EstadoPago:
        return self._estado

    def procesar_pago(self) -> bool:
        """Placeholder: en Paso 3 esto se conectará a una pasarela/servicio real."""
        exito = True
        if exito:
            self.confirmar_pago()
        else:
            self.rechazar_pago()
        return exito

    def confirmar_pago(self) -> None:
        self._estado = EstadoPago.APROBADO

    def rechazar_pago(self) -> None:
        self._estado = EstadoPago.RECHAZADO

    def __repr__(self) -> str:
        return f"Pago(${self._monto}, {self._estado.value})"


class Envio:
    def __init__(self, id: int, transportista: str, fecha_entrega_estimada: date):
        self._id = id
        self._fecha_despacho: Optional[date] = None
        self._fecha_entrega_estimada = fecha_entrega_estimada
        self._fecha_entrega_real: Optional[date] = None
        self._numero_seguimiento: Optional[str] = None
        self._transportista = transportista

    @property
    def id(self) -> int:
        return self._id

    @property
    def fecha_despacho(self) -> Optional[date]:
        return self._fecha_despacho

    @property
    def fecha_entrega_estimada(self) -> date:
        return self._fecha_entrega_estimada

    @property
    def fecha_entrega_real(self) -> Optional[date]:
        return self._fecha_entrega_real

    @property
    def numero_seguimiento(self) -> Optional[str]:
        return self._numero_seguimiento

    @property
    def transportista(self) -> str:
        return self._transportista

    def despachar(self) -> None:
        self._fecha_despacho = date.today()
        self._numero_seguimiento = f"{self._transportista[:3].upper()}-{self._id:06d}"

    def confirmar_entrega(self) -> None:
        self._fecha_entrega_real = date.today()

    def consultar_seguimiento(self) -> str:
        if self._numero_seguimiento is None:
            return "El pedido aún no ha sido despachado."
        return f"Seguimiento {self._numero_seguimiento} vía {self._transportista}"

    def __repr__(self) -> str:
        return f"Envio({self._numero_seguimiento or 'pendiente'})"

class Pedido:
    def __init__(self, id: int, cliente: "Cliente", direccion_entrega: DireccionEntrega,
                 detalles: list[DetallePedido]):
        if not detalles:
            raise ValueError("Un pedido debe tener al menos un detalle (multiplicidad 1..*).")
        self._id = id
        self._fecha = date.today()
        self._estado = EstadoPedido.CREADO
        self._cliente = cliente
        self._direccion_entrega = direccion_entrega
        self._detalles = list(detalles)
        self._total = 0.0
        self._pagos: list[Pago] = []
        self._envio: Optional[Envio] = None
        self.calcular_total()

    @property
    def id(self) -> int:
        return self._id

    @property
    def fecha(self) -> date:
        return self._fecha

    @property
    def estado(self) -> EstadoPedido:
        return self._estado

    @property
    def cliente(self) -> "Cliente":
        return self._cliente

    @property
    def direccion_entrega(self) -> DireccionEntrega:
        return self._direccion_entrega

    @property
    def detalles(self) -> list[DetallePedido]:
        return list(self._detalles)

    @property
    def total(self) -> float:
        return self._total

    @property
    def pagos(self) -> list[Pago]:
        return list(self._pagos)

    @property
    def envio(self) -> Optional[Envio]:
        return self._envio

    def calcular_total(self) -> float:
        self._total = sum(d.calcular_subtotal() for d in self._detalles)
        return self._total

    def confirmar_pedido(self) -> None:
        self.cambiar_estado(EstadoPedido.CONFIRMADO)

    def cambiar_estado(self, nuevo_estado: EstadoPedido) -> None:
        self._estado = nuevo_estado

    def cancelar(self) -> None:
        if self._estado == EstadoPedido.ENTREGADO:
            raise ValueError("No se puede cancelar un pedido ya entregado.")
        self.cambiar_estado(EstadoPedido.CANCELADO)

    def registrar_pago(self, monto: float, metodo_pago: str) -> Pago:
        pago = Pago(id=len(self._pagos) + 1, monto=monto, metodo_pago=metodo_pago)
        self._pagos.append(pago)
        return pago

    def generar_envio(self, transportista: str, fecha_entrega_estimada: date) -> Envio:
        self._envio = Envio(id=self._id, transportista=transportista,
                             fecha_entrega_estimada=fecha_entrega_estimada)
        self.cambiar_estado(EstadoPedido.ENVIADO)
        return self._envio

    def __repr__(self) -> str:
        return f"Pedido(#{self._id}, {self._estado.value}, total=${self._total})"


class CarritoDeCompra:
    def __init__(self, id: int):
        self._id = id
        self._fecha_creacion = date.today()
        self._items: list[ItemCarrito] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def fecha_creacion(self) -> date:
        return self._fecha_creacion

    @property
    def items(self) -> list[ItemCarrito]:
        return list(self._items)

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        if not producto.consultar_disponibilidad(cantidad):
            raise ValueError(f"Stock insuficiente para '{producto.nombre}'.")
        item_existente = self._buscar_item(producto)
        if item_existente:
            item_existente.cantidad += cantidad
        else:
            self._items.append(ItemCarrito(producto, cantidad))

    def actualizar_cantidad(self, producto: Producto, nueva_cantidad: int) -> None:
        item = self._buscar_item(producto)
        if item is None:
            raise ValueError("El producto no está en el carrito.")
        item.cantidad = nueva_cantidad  # valida > 0 internamente

    def eliminar_producto(self, producto: Producto) -> None:
        item = self._buscar_item(producto)
        if item is not None:
            self._items.remove(item)

    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self._items)

    def vaciar_carrito(self) -> None:
        self._items.clear()

    def generar_pedido(self, cliente: "Cliente", direccion_entrega: DireccionEntrega,
                       siguiente_id_pedido: int) -> Pedido:
        """Realiza la dependencia CarritoDeCompra ..> Pedido : crea."""
        if not self._items:
            raise ValueError("No se puede generar un pedido con el carrito vacío.")
        detalles = []
        for item in self._items:
            producto = item.producto
            producto.actualizar_stock(-item.cantidad)
            detalles.append(DetallePedido(producto, item.cantidad, item.precio_unitario))
        pedido = Pedido(id=siguiente_id_pedido, cliente=cliente,
                         direccion_entrega=direccion_entrega, detalles=detalles)
        self.vaciar_carrito()
        return pedido

    def _buscar_item(self, producto: Producto) -> Optional[ItemCarrito]:
        return next((i for i in self._items if i.producto is producto), None)

    def __repr__(self) -> str:
        return f"CarritoDeCompra({len(self._items)} items)"

class Cliente:
    def __init__(self, id: int, rut: str, nombre: str, email: str, telefono: str):
        self._id = id
        self._rut = self._validar_rut(rut)
        self._nombre = nombre
        self._email = self._validar_email(email)
        self._telefono = telefono
        self._direcciones: list[DireccionEntrega] = []
        self._carrito: Optional[CarritoDeCompra] = None
        self._pedidos: list[Pedido] = []
        self._contador_pedidos = 0

    @property
    def rut(self) -> str:
        return self._rut

    @staticmethod
    def _validar_rut(rut: str) -> str:
        rut_limpio = rut.replace(".", "").replace("-", "")
        if len(rut_limpio) < 8:
            raise ValueError("RUT inválido.")
        return rut

    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self._nombre = valor

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str) -> None:
        self._email = self._validar_email(valor)

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        self._telefono = valor

    @property
    def direcciones(self) -> list[DireccionEntrega]:
        return [d for d in self._direcciones if d.habilitada]

    @property
    def carrito(self) -> CarritoDeCompra:
        """Composición 0..1: se crea recién cuando el cliente lo necesita (lazy)."""
        if self._carrito is None:
            self._carrito = CarritoDeCompra(id=self._id)  # id provisorio (lo asignará la BD)
        return self._carrito

    @staticmethod
    def _validar_email(email: str) -> str:
        if "@" not in email:
            raise ValueError("Email inválido.")
        return email

    @classmethod
    def registrarse(cls, id: int, rut: str, nombre: str, email: str, telefono: str) -> "Cliente":
        return cls(id, rut, nombre, email, telefono)

    def actualizar_datos(self, nombre: str = None, email: str = None, telefono: str = None) -> None:
        if nombre is not None:
            self.nombre = nombre
        if email is not None:
            self.email = email
        if telefono is not None:
            self.telefono = telefono

    def agregar_direccion(self, direccion: DireccionEntrega) -> None:
        self._direcciones.append(direccion)

    def consultar_pedidos(self) -> list[Pedido]:
        return list(self._pedidos)

    def realizar_pedido(self, direccion_entrega: DireccionEntrega) -> Pedido:
        """Orquesta: toma el carrito actual y genera un pedido formal."""
        self._contador_pedidos += 1
        pedido = self.carrito.generar_pedido(
            cliente=self, direccion_entrega=direccion_entrega,
            siguiente_id_pedido=self._contador_pedidos,
        )
        self._pedidos.append(pedido)
        return pedido

    def __repr__(self) -> str:
        return f"Cliente({self._nombre})"


# =========================================================
# DEMO / PRUEBA MANUAL
# =========================================================

if __name__ == "__main__":
    categoria_tech = Categoria(1, "Tecnología", "Dispositivos electrónicos")
    mouse = Producto(1, "Mouse inalámbrico", "Mouse ergonómico", 12990, 50, categoria_tech)
    teclado = Producto(2, "Teclado mecánico", "Switches azules", 39990, 20, categoria_tech)

    cliente = Cliente.registrarse(1, "12345678-9", "Ana Pérez", "ana@correo.cl", "+56911111111")
    direccion = DireccionEntrega(1, "Av. Siempre Viva", "742", "Ñuñoa", "Santiago")
    cliente.agregar_direccion(direccion)

    cliente.carrito.agregar_producto(mouse, 2)
    cliente.carrito.agregar_producto(teclado, 1)
    print("Total carrito:", cliente.carrito.calcular_total())

    pedido = cliente.realizar_pedido(direccion)
    pedido.confirmar_pedido()
    print(pedido)

    pago = pedido.registrar_pago(monto=pedido.total, metodo_pago="tarjeta_credito")
    pago.procesar_pago()
    print(pago)

    envio = pedido.generar_envio("Chilexpress", date.today() + timedelta(days=3))
    envio.despachar()
    print(envio.consultar_seguimiento())

    print("Stock mouse restante:", mouse.stock_disponible)
    print("Productos en categoría:", categoria_tech.listar_productos())