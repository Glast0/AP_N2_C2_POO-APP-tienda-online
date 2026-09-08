CREATE DATABASE APPTIENDA;
USE APPTIENDA;

CREATE TABLE CATEGORIA(
    id_categoria INTEGER AUTO_INCREMENT,
    nombre_categoria VARCHAR(25) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,  

    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

CREATE TABLE PRODUCTO(
    id_producto INTEGER AUTO_INCREMENT,
    nombre_producto VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100),
    precio FLOAT,
    stock INTEGER,
    habilitado TINYINT NOT NULL DEFAULT 1, -- esto cuando se poone???

    CONSTRAINT pk_producto PRIMARY KEY (id_producto)
);

CREATE TABLE DIRECCION_ENTREGA(
    id_direccion_entrega INTEGER AUTO_INCREMENT,
    nombre_calle VARCHAR(50) NOT NULL,
    numero_casa INTEGER NOT NULL,
    cuidad VARCHAR(25),
    comuna VARCHAR(25)
    codigo_postal VARCHAR(10)
    habilitado TINYINT NOT NULL DEFAULT 1

    CONSTRAINT pk_direccion_entrega PRIMARY KEY (id_direccion_entrega)
);
CREATE TABLE ITEM_CARRITO(
    id_iteam_carrito INTEGER AUTO_INCREMENT,
    cantidad INTEGER NOT NULL,
    precio_unitario INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1

    CONSTRAINT pk_iteam_carrito PRIMARY KEY (id_iteam_carrito)
);

CREATE TABLE ITEM_CARRITO(
    id_iteam_pedido INTEGER AUTO_INCREMENT,
    cantidad INTEGER NOT NULL,
    precio_unitario INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1

    CONSTRAINT pk_iteam_producto PRIMARY KEY (id_iteam_producto)
);

CREATE TABLE PEDIDO(
    id_pedido INTEGER AUTO_INCREMENT,
    estado estado?,
    fecha DATE,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_pedido PRIMARY KEY (id_pedido)
);

CREATE TABLE CARRITO(
    id_carrito INTEGER AUTO_INCREMENT,
    fecha_creaccion DATE,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_carrito PRIMARY KEY (id_carrito)
);

CREATE TABLE CLIENTE(
    id_cliente INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50),
    email VARCHAR(100),
    telefono VARCHAR(20)
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_cliente PRIMARY KEY (id_cliente)
);

CREATE TABLE ESTADOPEDIDO(

);????
