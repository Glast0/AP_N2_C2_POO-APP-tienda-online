USE APPTIENDA;

-- =====================================================
-- 1. CATEGORIAS (20 registros)
-- =====================================================

INSERT INTO CATEGORIAS
(nombre_categoria, descripcion, habilitado)
VALUES
('Electrónica', 'Productos electrónicos y dispositivos tecnológicos', 1),
('Computación', 'Computadores, notebooks y accesorios', 1),
('Celulares', 'Teléfonos celulares y accesorios', 1),
('Hogar', 'Productos para el hogar', 1),
('Cocina', 'Utensilios y electrodomésticos de cocina', 1),
('Ropa', 'Vestuario para hombres y mujeres', 1),
('Calzado', 'Zapatos, zapatillas y sandalias', 1),
('Deportes', 'Artículos deportivos', 1),
('Juguetes', 'Juguetes para niños', 1),
('Libros', 'Libros y material de lectura', 1),
('Belleza', 'Productos de belleza y cuidado personal', 1),
('Jardinería', 'Herramientas y productos de jardinería', 1),
('Automóvil', 'Accesorios para vehículos', 1),
('Oficina', 'Artículos para oficina', 1),
('Mascotas', 'Productos para mascotas', 1),
('Audio', 'Audífonos, parlantes y equipos de audio', 1),
('Video', 'Televisores y dispositivos de video', 1),
('Iluminación', 'Lámparas y productos de iluminación', 1),
('Accesorios', 'Accesorios variados', 1),
('Gaming', 'Productos para videojuegos', 1);


-- =====================================================
-- 2. PRODUCTOS (20 registros)
-- =====================================================

INSERT INTO PRODUCTOS
(id_categoria, nombre_producto, descripcion, precio, stock_disponible, habilitado)
VALUES
(1, 'Smart TV Samsung 50"', 'Televisor Smart TV 4K de 50 pulgadas', 399990, 15, 1),
(2, 'Notebook Lenovo IdeaPad', 'Notebook Lenovo con 8GB RAM y 512GB SSD', 549990, 10, 1),
(3, 'iPhone 15', 'Smartphone Apple iPhone 15 de 128GB', 799990, 8, 1),
(4, 'Aspiradora Thomas', 'Aspiradora para uso doméstico', 89990, 20, 1),
(5, 'Freidora de Aire', 'Freidora de aire de 4 litros', 69990, 25, 1),
(6, 'Polera Adidas', 'Polera deportiva Adidas', 29990, 30, 1),
(7, 'Zapatillas Nike Air', 'Zapatillas deportivas Nike', 89990, 18, 1),
(8, 'Balón de Fútbol', 'Balón de fútbol profesional', 24990, 35, 1),
(9, 'LEGO City', 'Set de construcción LEGO City', 39990, 12, 1),
(10, 'El Principito', 'Libro clásico de Antoine de Saint-Exupéry', 12990, 40, 1),
(11, 'Perfume Hombre', 'Perfume masculino 100 ml', 49990, 15, 1),
(12, 'Kit Jardinería', 'Set de herramientas para jardinería', 29990, 20, 1),
(13, 'Cargador Auto USB', 'Cargador USB para automóvil', 9990, 50, 1),
(14, 'Silla de Oficina', 'Silla ergonómica para escritorio', 119990, 10, 1),
(15, 'Cama para Perro', 'Cama acolchada para mascotas', 34990, 15, 1),
(16, 'Audífonos Bluetooth', 'Audífonos inalámbricos Bluetooth', 45990, 25, 1),
(17, 'Chromecast', 'Dispositivo de streaming multimedia', 39990, 20, 1),
(18, 'Lámpara LED', 'Lámpara LED de escritorio', 19990, 30, 1),
(19, 'Mochila Urbana', 'Mochila para uso diario', 29990, 25, 1),
(20, 'Control Xbox', 'Control inalámbrico para Xbox', 64990, 15, 1);


-- =====================================================
-- 3. CLIENTES (20 registros)
-- =====================================================

INSERT INTO CLIENTES
(rut, nombre, email, telefono, habilitado)
VALUES
('11111111-1', 'Juan Pérez', 'juan.perez@gmail.com', '+56911111111', 1),
('22222222-2', 'María González', 'maria.gonzalez@gmail.com', '+56922222222', 1),
('33333333-3', 'Pedro Rodríguez', 'pedro.rodriguez@gmail.com', '+56933333333', 1),
('44444444-4', 'Ana Martínez', 'ana.martinez@gmail.com', '+56944444444', 1),
('55555555-5', 'Carlos Soto', 'carlos.soto@gmail.com', '+56955555555', 1),
('66666666-6', 'Laura Contreras', 'laura.contreras@gmail.com', '+56966666666', 1),
('77777777-7', 'Diego Silva', 'diego.silva@gmail.com', '+56977777777', 1),
('88888888-8', 'Camila Torres', 'camila.torres@gmail.com', '+56988888888', 1),
('99999999-9', 'Felipe Rojas', 'felipe.rojas@gmail.com', '+56999999999', 1),
('10101010-1', 'Sofía Morales', 'sofia.morales@gmail.com', '+56910101010', 1),
('12121212-2', 'Andrés Fuentes', 'andres.fuentes@gmail.com', '+56912121212', 1),
('13131313-3', 'Valentina Castro', 'valentina.castro@gmail.com', '+56913131313', 1),
('14141414-4', 'Sebastián Vargas', 'sebastian.vargas@gmail.com', '+56914141414', 1),
('15151515-5', 'Daniela Espinoza', 'daniela.espinoza@gmail.com', '+56915151515', 1),
('16161616-6', 'Jorge Muñoz', 'jorge.munoz@gmail.com', '+56916161616', 1),
('17171717-7', 'Fernanda Reyes', 'fernanda.reyes@gmail.com', '+56917171717', 1),
('18181818-8', 'Nicolás Araya', 'nicolas.araya@gmail.com', '+56918181818', 1),
('19191919-9', 'Paula Navarro', 'paula.navarro@gmail.com', '+56919191919', 1),
('20202020-0', 'Ricardo Paredes', 'ricardo.paredes@gmail.com', '+56920202020', 1),
('21212121-1', 'Constanza Vidal', 'constanza.vidal@gmail.com', '+56921212121', 1);


-- =====================================================
-- 4. DIRECCION_ENTREGAS (20 registros)
-- =====================================================

INSERT INTO DIRECCION_ENTREGAS
(id_cliente, calle, numero, comuna, ciudad, habilitado)
VALUES
(1, 'Av. Providencia', '1234', 'Providencia', 'Santiago', 1),
(2, 'Av. Las Condes', '2450', 'Las Condes', 'Santiago', 1),
(3, 'Av. Vicuña Mackenna', '1560', 'Ñuñoa', 'Santiago', 1),
(4, 'Irarrázaval', '3250', 'Ñuñoa', 'Santiago', 1),
(5, 'Av. Apoquindo', '4500', 'Las Condes', 'Santiago', 1),
(6, 'Gran Avenida', '2100', 'La Cisterna', 'Santiago', 1),
(7, 'Av. La Florida', '8500', 'La Florida', 'Santiago', 1),
(8, 'Av. Macul', '2800', 'Macul', 'Santiago', 1),
(9, 'Av. Grecia', '1650', 'Peñalolén', 'Santiago', 1),
(10, 'Av. Independencia', '1200', 'Independencia', 'Santiago', 1),
(11, 'Av. Brasil', '850', 'Santiago Centro', 'Santiago', 1),
(12, 'San Diego', '1450', 'Santiago Centro', 'Santiago', 1),
(13, 'Av. Matta', '2200', 'Santiago Centro', 'Santiago', 1),
(14, 'Av. Pajaritos', '3400', 'Maipú', 'Santiago', 1),
(15, 'Camino Melipilla', '5600', 'Maipú', 'Santiago', 1),
(16, 'Av. Recoleta', '1850', 'Recoleta', 'Santiago', 1),
(17, 'Av. Santa Rosa', '3200', 'San Miguel', 'Santiago', 1),
(18, 'Av. Departamental', '2700', 'San Miguel', 'Santiago', 1),
(19, 'Av. Quilín', '4100', 'Peñalolén', 'Santiago', 1),
(20, 'Av. Tobalaba', '2900', 'Providencia', 'Santiago', 1);


-- =====================================================
-- 5. CARRITOS (20 registros)
-- =====================================================

INSERT INTO CARRITOS
(id_cliente, fecha_creacion, habilitado)
VALUES
(1, '2026-09-01', 1),
(2, '2026-09-01', 1),
(3, '2026-09-02', 1),
(4, '2026-09-02', 1),
(5, '2026-09-03', 1),
(6, '2026-09-03', 1),
(7, '2026-09-04', 1),
(8, '2026-09-04', 1),
(9, '2026-09-05', 1),
(10, '2026-09-05', 1),
(11, '2026-09-06', 1),
(12, '2026-09-06', 1),
(13, '2026-09-07', 1),
(14, '2026-09-07', 1),
(15, '2026-09-08', 1),
(16, '2026-09-08', 1),
(17, '2026-09-09', 1),
(18, '2026-09-09', 1),
(19, '2026-09-10', 1),
(20, '2026-09-10', 1);


-- =====================================================
-- 6. ITEM_CARRITOS (20 registros)
-- =====================================================

INSERT INTO ITEM_CARRITOS
(id_carrito, id_producto, cantidad, precio_unitario, habilitado)
VALUES
(1, 3, 1, 799990, 1),
(2, 7, 2, 89990, 1),
(3, 2, 1, 549990, 1),
(4, 10, 3, 12990, 1),
(5, 1, 1, 399990, 1),
(6, 16, 2, 45990, 1),
(7, 5, 1, 69990, 1),
(8, 20, 1, 64990, 1),
(9, 8, 2, 24990, 1),
(10, 14, 1, 119990, 1),
(11, 11, 1, 49990, 1),
(12, 15, 1, 34990, 1),
(13, 4, 1, 89990, 1),
(14, 18, 2, 19990, 1),
(15, 19, 1, 29990, 1),
(16, 6, 2, 29990, 1),
(17, 17, 1, 39990, 1),
(18, 12, 1, 29990, 1),
(19, 9, 2, 39990, 1),
(20, 13, 3, 9990, 1);


-- =====================================================
-- 7. PEDIDOS (20 registros)
-- Estados:
-- 1 = CREADO
-- 2 = CONFIRMADO
-- 3 = EN_PREPARACION
-- 4 = ENVIADO
-- 5 = ENTREGADO
-- 6 = CANCELADO
-- =====================================================

INSERT INTO PEDIDOS
(id_cliente, id_direccion_entrega, fecha, estado_pedidos, total, habilitado)
VALUES
(1, 1, '2026-09-01', 5, 799990, 1),
(2, 2, '2026-09-02', 5, 179980, 1),
(3, 3, '2026-09-03', 4, 549990, 1),
(4, 4, '2026-09-04', 5, 38970, 1),
(5, 5, '2026-09-05', 3, 399990, 1),
(6, 6, '2026-09-06', 4, 91980, 1),
(7, 7, '2026-09-07', 2, 69990, 1),
(8, 8, '2026-09-08', 5, 64990, 1),
(9, 9, '2026-09-09', 5, 49980, 1),
(10, 10, '2026-09-10', 3, 119990, 1),
(11, 11, '2026-09-11', 2, 49990, 1),
(12, 12, '2026-09-11', 5, 34990, 1),
(13, 13, '2026-09-12', 4, 89990, 1),
(14, 14, '2026-09-12', 1, 39980, 1),
(15, 15, '2026-09-13', 6, 29990, 1),
(16, 16, '2026-09-13', 5, 59980, 1),
(17, 17, '2026-09-14', 4, 39990, 1),
(18, 18, '2026-09-14', 3, 29990, 1),
(19, 19, '2026-09-15', 2, 79980, 1),
(20, 20, '2026-09-15', 1, 29970, 1);


-- =====================================================
-- 8. DETALLE_PEDIDOS (20 registros)
-- =====================================================

INSERT INTO DETALLE_PEDIDOS
(id_pedido, id_producto, cantidad, precio_unitario, habilitado)
VALUES
(1, 3, 1, 799990, 1),
(2, 7, 2, 89990, 1),
(3, 2, 1, 549990, 1),
(4, 10, 3, 12990, 1),
(5, 1, 1, 399990, 1),
(6, 16, 2, 45990, 1),
(7, 5, 1, 69990, 1),
(8, 20, 1, 64990, 1),
(9, 8, 2, 24990, 1),
(10, 14, 1, 119990, 1),
(11, 11, 1, 49990, 1),
(12, 15, 1, 34990, 1),
(13, 4, 1, 89990, 1),
(14, 18, 2, 19990, 1),
(15, 19, 1, 29990, 1),
(16, 6, 2, 29990, 1),
(17, 17, 1, 39990, 1),
(18, 12, 1, 29990, 1),
(19, 9, 2, 39990, 1),
(20, 13, 3, 9990, 1);


-- =====================================================
-- 9. PAGOS (20 registros)
-- Estados:
-- 1 = PENDIENTE
-- 2 = APROBADO
-- 3 = RECHAZADO
-- 4 = REEMBOLSADO
-- =====================================================

INSERT INTO PAGOS
(id_pedido, monto, fecha, metodo_pago, estado_pagos, habilitado)
VALUES
(1, 799990, '2026-09-01 10:15:00', 'Tarjeta de crédito', 2, 1),
(2, 179980, '2026-09-02 11:20:00', 'Tarjeta de débito', 2, 1),
(3, 549990, '2026-09-03 12:10:00', 'Transferencia bancaria', 2, 1),
(4, 38970, '2026-09-04 13:30:00', 'Tarjeta de crédito', 2, 1),
(5, 399990, '2026-09-05 14:15:00', 'WebPay', 2, 1),
(6, 91980, '2026-09-06 15:00:00', 'Tarjeta de débito', 2, 1),
(7, 69990, '2026-09-07 15:45:00', 'Tarjeta de crédito', 2, 1),
(8, 64990, '2026-09-08 16:10:00', 'WebPay', 2, 1),
(9, 49980, '2026-09-09 16:40:00', 'Transferencia bancaria', 2, 1),
(10, 119990, '2026-09-10 17:00:00', 'Tarjeta de crédito', 2, 1),
(11, 49990, '2026-09-11 10:20:00', 'Tarjeta de débito', 2, 1),
(12, 34990, '2026-09-11 11:30:00', 'WebPay', 2, 1),
(13, 89990, '2026-09-12 12:15:00', 'Tarjeta de crédito', 2, 1),
(14, 39980, '2026-09-12 13:20:00', 'Tarjeta de débito', 1, 1),
(15, 29990, '2026-09-13 14:00:00', 'Tarjeta de crédito', 4, 1),
(16, 59980, '2026-09-13 15:15:00', 'WebPay', 2, 1),
(17, 39990, '2026-09-14 16:00:00', 'Transferencia bancaria', 2, 1),
(18, 29990, '2026-09-14 16:45:00', 'Tarjeta de crédito', 2, 1),
(19, 79980, '2026-09-15 10:30:00', 'Tarjeta de débito', 1, 1),
(20, 29970, '2026-09-15 11:00:00', 'WebPay', 1, 1);


-- =====================================================
-- 10. ENVIOS (20 registros)
-- =====================================================

INSERT INTO ENVIOS
(id_pedido, fecha_despacho, fecha_entrega_estimada,
 fecha_entrega_real, numero_seguimiento, transportista, habilitado)
VALUES
(1, '2026-09-02', '2026-09-04', '2026-09-04', 'STK100001', 'Chilexpress', 1),
(2, '2026-09-03', '2026-09-05', '2026-09-05', 'STK100002', 'Blue Express', 1),
(3, '2026-09-04', '2026-09-07', NULL, 'STK100003', 'Correos de Chile', 1),
(4, '2026-09-05', '2026-09-07', '2026-09-07', 'STK100004', 'Chilexpress', 1),
(5, NULL, '2026-09-09', NULL, 'STK100005', 'Blue Express', 1),
(6, '2026-09-07', '2026-09-10', NULL, 'STK100006', 'Starken', 1),
(7, NULL, '2026-09-11', NULL, NULL, NULL, 1),
(8, '2026-09-09', '2026-09-11', '2026-09-11', 'STK100008', 'Chilexpress', 1),
(9, '2026-09-10', '2026-09-12', '2026-09-12', 'STK100009', 'Blue Express', 1),
(10, NULL, '2026-09-14', NULL, NULL, NULL, 1),
(11, NULL, '2026-09-15', NULL, NULL, NULL, 1),
(12, '2026-09-12', '2026-09-15', '2026-09-15', 'STK100012', 'Starken', 1),
(13, '2026-09-13', '2026-09-16', NULL, 'STK100013', 'Chilexpress', 1),
(14, NULL, '2026-09-17', NULL, NULL, NULL, 1),
(15, NULL, NULL, NULL, NULL, NULL, 1),
(16, '2026-09-14', '2026-09-17', '2026-09-17', 'STK100016', 'Blue Express', 1),
(17, '2026-09-15', '2026-09-18', NULL, 'STK100017', 'Starken', 1),
(18, NULL, '2026-09-19', NULL, NULL, NULL, 1),
(19, NULL, '2026-09-20', NULL, NULL, NULL, 1),
(20, NULL, '2026-09-21', NULL, NULL, NULL, 1);
