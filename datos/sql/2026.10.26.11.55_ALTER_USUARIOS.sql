ALTER TABLE usuarios Modify colum rut char(12);
ALTER TABLE usuarios ADD password VARCHAR(60) NULL;
ALTER TABLE usuarios ENGINE=InnoDB;
ALTER TABLE usuarios ADD unique(correo);




Create table usuarios(
    id_usuario INTEGER AUTO_INCREMENT,
    rut Varchar(11) NULL,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    pais INTEGER NULL,
    fecha_nacimiento DATE NULL,
    genero INTEGER NOT NULL,
    fecha_incorporacion DATE NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_usuarios PRIMARY KEY (id_usuario),

) COMMENT = 'Tabla de usuarios de sistema.'

Create table roles(
    id_rol INTEGER AUTO_INCREMENT,
    tipo_rol,
    constraseña
    


)