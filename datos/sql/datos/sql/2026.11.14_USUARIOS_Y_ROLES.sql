USE APPTIENDA;

DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS roles;

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT,
    rut CHAR(12) NOT NULL,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    correo VARCHAR(191) NOT NULL,
    fecha_nacimiento DATE NULL,
    fecha_incorporacion DATE NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    password VARCHAR(60) NOT NULL,

    CONSTRAINT pk_usuario PRIMARY KEY (id_usuario),
    CONSTRAINT uq_usuario_rut UNIQUE (rut),
    CONSTRAINT uq_usuario_correo UNIQUE (correo)
) COMMENT = 'Tabla de usuarios de sistema. Administradores de la tienda';