CREATE DATABASE IF NOT EXISTS APPTIENDA;
USE APPTIENDA;

-- 1. Categorías de productos
CREATE TABLE CATEGORIAS (
    id_categoria INT AUTO_INCREMENT,
    nombre_categoria VARCHAR(50) NOT NULL,
    descripcion VARCHAR(150),
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

-- 2. Catálogo de Productos
CREATE TABLE PRODUCTOS (
    id_producto INT AUTO_INCREMENT,
    id_categoria INT NOT NULL,
    nombre_producto VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio FLOAT NOT NULL,
    stock_disponible INT NOT NULL DEFAULT 0,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_producto PRIMARY KEY (id_producto),
    CONSTRAINT fk_producto_categoria FOREIGN KEY (id_categoria) REFERENCES CATEGORIAS(id_categoria)
);

-- 3. Clientes
CREATE TABLE CLIENTES (
    id_cliente INT AUTO_INCREMENT,
    rut VARCHAR(12) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_cliente PRIMARY KEY (id_cliente)
);

-- 4. Direcciones guardadas por los clientes
CREATE TABLE DIRECCION_ENTREGAS (
    id_direccion_entrega INT AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    calle VARCHAR(100) NOT NULL,
    numero VARCHAR(15) NOT NULL,
    comuna VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_direccion_entrega PRIMARY KEY (id_direccion_entrega),
    CONSTRAINT fk_direccion_cliente FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente)
);

-- 5. Carrito de Compras activo del usuario (1 a 0..1)
CREATE TABLE CARRITOS (
    id_carrito INT AUTO_INCREMENT,
    id_cliente INT NOT NULL UNIQUE,
    fecha_creacion DATE NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_carrito PRIMARY KEY (id_carrito),
    CONSTRAINT fk_carrito_cliente FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente)
);

-- 6. Items dentro del Carrito
CREATE TABLE ITEM_CARRITOS (
    id_item_carrito INT AUTO_INCREMENT,
    id_carrito INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 1,
    precio_unitario FLOAT NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_item_carrito PRIMARY KEY (id_item_carrito),
    CONSTRAINT fk_item_carrito FOREIGN KEY (id_carrito) REFERENCES CARRITOS(id_carrito),
    CONSTRAINT fk_item_producto FOREIGN KEY (id_producto) REFERENCES PRODUCTOS(id_producto)
);

-- 7. Pedidos realizados
CREATE TABLE PEDIDOS (
    id_pedido INT AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_direccion_entrega INT NOT NULL,
    fecha DATE NOT NULL,
    estado ENUM('CREADO', 'CONFIRMADO', 'EN_PREPARACION', 'ENVIADO', 'ENTREGADO', 'CANCELADO') NOT NULL DEFAULT 'CREADO',
    total FLOAT NOT NULL DEFAULT 0,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_pedido PRIMARY KEY (id_pedido),
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente),
    CONSTRAINT fk_pedido_direccion FOREIGN KEY (id_direccion_entrega) REFERENCES DIRECCION_ENTREGAS(id_direccion_entrega)
);

-- 8. Detalle/Líneas de los Pedidos
CREATE TABLE DETALLE_PEDIDOS (
    id_detalle_pedido INT AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario FLOAT NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_detalle_pedido PRIMARY KEY (id_detalle_pedido),
    CONSTRAINT fk_detalle_pedido FOREIGN KEY (id_pedido) REFERENCES PEDIDOS(id_pedido),
    CONSTRAINT fk_detalle_producto FOREIGN KEY (id_producto) REFERENCES PRODUCTOS(id_producto)
);

-- 9. Registro de Pagos
CREATE TABLE PAGOS (
    id_pago INT AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    monto FLOAT NOT NULL,
    fecha DATETIME NOT NULL,
    metodo_pago VARCHAR(50) NOT NULL,
    estado ENUM('PENDIENTE', 'APROBADO', 'RECHAZADO', 'REEMBOLSADO') NOT NULL DEFAULT 'PENDIENTE',
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_pago PRIMARY KEY (id_pago),
    CONSTRAINT fk_pago_pedido FOREIGN KEY (id_pedido) REFERENCES PEDIDOS(id_pedido)
);

-- 10. Información de Envíos (Relación 1 a 0..1 con Pedido)
CREATE TABLE ENVIOS (
    id_envio INT AUTO_INCREMENT,
    id_pedido INT NOT NULL UNIQUE,
    fecha_despacho DATE,
    fecha_entrega_estimada DATE,
    fecha_entrega_real DATE,
    numero_seguimiento VARCHAR(100),
    transportista VARCHAR(50),
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_envio PRIMARY KEY (id_envio),
    CONSTRAINT fk_envio_pedido FOREIGN KEY (id_pedido) REFERENCES PEDIDOS(id_pedido)
);