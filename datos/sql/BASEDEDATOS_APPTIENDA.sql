CREATE DATABASE APPTIENDA;
USE APPTIENDA;

-- 1. Categorías de productos
CREATE TABLE CATEGORIAS (
    id_categoria INT AUTO_INCREMENT,
    nombre_categoria VARCHAR(50) NOT NULL,
    descripcion VARCHAR(150),
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

-- 2. Catálogo de productos
CREATE TABLE PRODUCTOS (
    id_producto INT AUTO_INCREMENT,
    id_categoria INT NOT NULL,
    nombre_producto VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock_disponible INT NOT NULL DEFAULT 0,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_producto PRIMARY KEY (id_producto),
    CONSTRAINT fk_producto_categoria FOREIGN KEY (id_categoria) REFERENCES CATEGORIAS(id_categoria)
);

-- 3. Clientes
CREATE TABLE CLIENTES (
    id_cliente INT AUTO_INCREMENT,
    rut VARCHAR(12) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_cliente PRIMARY KEY (id_cliente)
);

-- 4. Direcciones de entrega
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

-- 5. Carrito de compras (0..1 por cliente -> UNIQUE)
CREATE TABLE CARRITOS (
    id_carrito INT AUTO_INCREMENT,
    id_cliente INT NOT NULL UNIQUE,
    fecha_creacion DATE NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_carrito PRIMARY KEY (id_carrito),
    CONSTRAINT fk_carrito_cliente FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente)
);

-- 6. Items del carrito (clase de asociación CarritoDeCompra <-> Producto)
CREATE TABLE ITEM_CARRITOS (
    id_item_carrito INT AUTO_INCREMENT,
    id_carrito INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 1,
    precio_unitario DECIMAL(10,2) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_item_carrito PRIMARY KEY (id_item_carrito),
    CONSTRAINT fk_item_carrito FOREIGN KEY (id_carrito) REFERENCES CARRITOS(id_carrito),
    CONSTRAINT fk_item_producto FOREIGN KEY (id_producto) REFERENCES PRODUCTOS(id_producto)
);

-- 7. Catálogo de estados de pedido (espejo relacional de EstadoPedido)
CREATE TABLE ESTADOS_PEDIDO (
    id_estado_pedido INT,
    nombre VARCHAR(20) NOT NULL UNIQUE,

    CONSTRAINT pk_estado_pedido PRIMARY KEY (id_estado_pedido)
);
INSERT INTO ESTADOS_PEDIDO (id_estado_pedido, nombre) VALUES
    (1, 'CREADO'), (2, 'CONFIRMADO'), (3, 'EN_PREPARACION'),
    (4, 'ENVIADO'), (5, 'ENTREGADO'), (6, 'CANCELADO');

-- 8. Pedidos realizados
CREATE TABLE PEDIDOS (
    id_pedido INT AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_direccion_entrega INT NOT NULL,
    id_estado_pedido INT NOT NULL DEFAULT 1,
    fecha DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL DEFAULT 0,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_pedido PRIMARY KEY (id_pedido),
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente),
    CONSTRAINT fk_pedido_direccion FOREIGN KEY (id_direccion_entrega) REFERENCES DIRECCION_ENTREGAS(id_direccion_entrega),
    CONSTRAINT fk_pedido_estado FOREIGN KEY (id_estado_pedido) REFERENCES ESTADOS_PEDIDO(id_estado_pedido)
);

-- 9. Detalle/líneas de los pedidos (clase de asociación Pedido <-> Producto)
CREATE TABLE DETALLE_PEDIDOS (
    id_detalle_pedido INT AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_detalle_pedido PRIMARY KEY (id_detalle_pedido),
    CONSTRAINT fk_detalle_pedido FOREIGN KEY (id_pedido) REFERENCES PEDIDOS(id_pedido),
    CONSTRAINT fk_detalle_producto FOREIGN KEY (id_producto) REFERENCES PRODUCTOS(id_producto)
);

-- 10. Catálogo de estados de pago
CREATE TABLE ESTADOS_PAGO (
    id_estado_pago INT,
    nombre VARCHAR(20) NOT NULL UNIQUE,

    CONSTRAINT pk_estado_pago PRIMARY KEY (id_estado_pago)
);
INSERT INTO ESTADOS_PAGO (id_estado_pago, nombre) VALUES
    (1, 'PENDIENTE'), (2, 'APROBADO'), (3, 'RECHAZADO'), (4, 'REEMBOLSADO');

-- 11. Registro de pagos
CREATE TABLE PAGOS (
    id_pago INT AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_estado_pago INT NOT NULL DEFAULT 1,
    monto DECIMAL(10,2) NOT NULL,
    fecha DATETIME NOT NULL,
    metodo_pago VARCHAR(50) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_pago PRIMARY KEY (id_pago),
    CONSTRAINT fk_pago_pedido FOREIGN KEY (id_pedido) REFERENCES PEDIDOS(id_pedido),
    CONSTRAINT fk_pago_estado FOREIGN KEY (id_estado_pago) REFERENCES ESTADOS_PAGO(id_estado_pago)
);

-- 12. Información de envíos
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