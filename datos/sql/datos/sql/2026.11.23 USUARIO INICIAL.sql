-- Usuario inicial del sistema (administrador)
-- Ejecutar DESPUES de crear la tabla `usuarios` (2026.11.14_USUARIOS_Y_ROLES.sql).
--
-- Credenciales de acceso:
--   correo:     admin@apptienda.cl
--   contrasena: Admin123!
-- Cambiar la contrasena despues del primer ingreso.
-- La contrasena NO se guarda en texto plano: `password` contiene un hash BCrypt.

USE APPTIENDA;

INSERT INTO usuarios (rut, nombre, apellido, correo, fecha_nacimiento, fecha_incorporacion, habilitado, password)
VALUES (
    '11.111.111-1',
    'Admin',
    'Sistema',
    'admin@apptienda.cl',
    NULL,
    CURDATE(),
    1,
    '$2b$12$Osr/QblK6RtqEhHRlPNxUuRoGAcJgCiD7zNHorOLpI/XNj9zGxnsi'
);