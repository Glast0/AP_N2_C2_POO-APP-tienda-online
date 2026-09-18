USE APPTIENDA;

-- ============================================================
-- 1. CATEGORIAS
-- ============================================================

INSERT INTO CATEGORIAS
    (id_categoria, nombre_categoria, descripcion, habilitado)
VALUES
    (1, 'Computación',
        'Equipos y accesorios principales para computación.',
        1),

    (2, 'Periféricos',
        'Dispositivos de entrada, salida y comunicación.',
        1),

    (3, 'Oficina y Mobiliario',
        'Mobiliario y elementos para espacios de trabajo.',
        1),

    (4, 'Almacenamiento y Componentes',
        'Memorias, discos y componentes para computadores.',
        1),

    (5, 'Móviles',
        'Teléfonos, tablets y accesorios móviles.',
        1),

    (6, 'Audio',
        'Audífonos, parlantes y equipos de audio.',
        1),

    (7, 'Fotografía y Creación',
        'Equipos y accesorios para fotografía y creación de contenido.',
        1),

    (8, 'Hogar y Conectividad',
        'Productos inteligentes y de conectividad para el hogar.',
        0);


-- ============================================================
-- 2. PRODUCTOS
-- ============================================================

INSERT INTO PRODUCTOS
    (id_producto, id_categoria, nombre_producto, descripcion,
     precio, stock_disponible, habilitado)
VALUES
    (1, 1, 'Notebook Pro 15',
        'Notebook de 15 pulgadas con 16 GB de RAM y SSD de 512 GB.',
        549990.00, 12, 1),

    (2, 1, 'Monitor IPS 27',
        'Monitor IPS de 27 pulgadas con resolución Full HD.',
        189990.00, 20, 1),

    (3, 1, 'Mini PC Office',
        'Mini computador compacto para trabajo y estudio.',
        329990.00, 8, 1),

    (4, 2, 'Teclado Mecánico RGB',
        'Teclado mecánico con iluminación RGB.',
        39990.00, 35, 1),

    (5, 2, 'Mouse Inalámbrico Pro',
        'Mouse inalámbrico ergonómico de alta precisión.',
        49990.00, 40, 1),

    (6, 2, 'Webcam Full HD',
        'Cámara web Full HD con micrófono incorporado.',
        29990.00, 25, 1),

    (7, 3, 'Silla Ergonómica',
        'Silla de oficina con soporte lumbar regulable.',
        179990.00, 10, 1),

    (8, 3, 'Escritorio Ejecutivo',
        'Escritorio de madera con cajones y acabado mate.',
        129990.00, 7, 1),

    (9, 4, 'SSD NVMe 1 TB',
        'Unidad SSD NVMe de 1 TB para almacenamiento rápido.',
        79990.00, 30, 1),

    (10, 4, 'HDD 2 TB',
        'Disco duro interno de 2 TB.',
        69990.00, 18, 1),

    (11, 4, 'Memoria RAM 16 GB',
        'Memoria RAM DDR4 de 16 GB.',
        45990.00, 22, 1),

    (12, 4, 'Tarjeta Gráfica RTX',
        'Tarjeta gráfica dedicada para videojuegos y creación.',
        799990.00, 5, 1),

    (13, 5, 'Smartphone X Pro',
        'Teléfono inteligente con pantalla AMOLED de 6,5 pulgadas.',
        399990.00, 15, 1),

    (14, 5, 'Tablet 11 Pro',
        'Tablet de 11 pulgadas para estudio y entretenimiento.',
        249990.00, 11, 1),

    (15, 5, 'Smartwatch Active',
        'Reloj inteligente con monitoreo deportivo y notificaciones.',
        89990.00, 17, 1),

    (16, 5, 'Powerbank 20000 mAh',
        'Batería externa de alta capacidad con carga rápida.',
        24990.00, 28, 1),

    (17, 6, 'Audífonos Bluetooth ANC',
        'Audífonos inalámbricos con cancelación activa de ruido.',
        69990.00, 19, 1),

    (18, 6, 'Parlante Bluetooth Max',
        'Parlante portátil Bluetooth de alta potencia.',
        59990.00, 0, 0),

    (19, 7, 'Cámara Mirrorless 24 MP',
        'Cámara sin espejo de 24 megapíxeles para fotografía.',
        429990.00, 6, 1),

    (20, 7, 'Trípode Profesional',
        'Trípode de aluminio para cámaras y teléfonos.',
        39990.00, 14, 1),

    (21, 7, 'Micrófono USB Studio',
        'Micrófono USB para streaming, voz y grabación.',
        89990.00, 9, 1),

    (22, 8, 'Router Wi-Fi 6',
        'Router inalámbrico compatible con Wi-Fi 6.',
        79990.00, 0, 0),

    (23, 8, 'Enchufe Inteligente',
        'Enchufe inteligente controlable mediante aplicación.',
        19990.00, 0, 0),

    (24, 8, 'Impresora Multifunción',
        'Impresora multifunción con conexión inalámbrica.',
        159990.00, 0, 0);


-- ============================================================
-- 3. CLIENTES
-- ============================================================

INSERT INTO CLIENTES
    (id_cliente, rut, nombre, email, telefono, habilitado)
VALUES
    (1, '12.345.678-5',
        'Felipe González',
        'felipe.gonzalez@email.com',
        '+56911111111',
        1),

    (2, '15.345.678-K',
        'Camila Rojas',
        'camila.rojas@email.com',
        '+56922222222',
        1),

    (3, '17.123.456-5',
        'Matías Herrera',
        'matias.herrera@email.com',
        '+56933333333',
        1),

    (4, '18.543.210-6',
        'Valentina Soto',
        'valentina.soto@email.com',
        '+56944444444',
        1),

    (5, '20.123.456-5',
        'Diego Contreras',
        'diego.contreras@email.com',
        '+56955555555',
        1),

    (6, '22.123.456-1',
        'Antonia Pérez',
        'antonia.perez@email.com',
        '+56966666666',
        1),

    (7, '9.876.543-3',
        'Javier Muñoz',
        'javier.munoz@email.com',
        '+56977777777',
        1),

    (8, '11.223.344-K',
        'Sofía Torres',
        'sofia.torres@email.com',
        '+56988888888',
        1),

    (9, '14.285.714-6',
        'Nicolás Fuentes',
        'nicolas.fuentes@email.com',
        '+56999999999',
        1),

    (10, '16.789.012-1',
        'Daniela Silva',
        'daniela.silva@email.com',
        '+56910101010',
        0);


-- ============================================================
-- 4. DIRECCIONES DE ENTREGA
-- ============================================================

INSERT INTO DIRECCION_ENTREGAS
    (id_direccion_entrega, id_cliente, calle, numero,
     comuna, ciudad, habilitado)
VALUES
    (1, 1, 'Av. Providencia', '1234',
        'Providencia', 'Santiago', 1),

    (2, 1, 'Pasaje Los Alerces', '88',
        'Ñuñoa', 'Santiago', 1),

    (3, 2, 'Av. Vicuña Mackenna', '2250',
        'Viña del Mar', 'Viña del Mar', 1),

    (4, 2, 'Calle Balmaceda', '451',
        'Valparaíso', 'Valparaíso', 1),

    (5, 3, 'Av. Grecia', '1750',
        'La Florida', 'Santiago', 1),

    (6, 4, 'Av. Las Condes', '8400',
        'Las Condes', 'Santiago', 1),

    (7, 4, 'Calle El Alba', '125',
        'Lo Barnechea', 'Santiago', 1),

    (8, 5, 'Av. Ossa', '3150',
        'Macul', 'Santiago', 1),

    (9, 6, 'Av. Pajaritos', '1420',
        'Maipú', 'Santiago', 1),

    (10, 6, 'Calle Maipú', '650',
        'Estación Central', 'Santiago', 0),

    (11, 7, 'Av. Irarrázaval', '3020',
        'Ñuñoa', 'Santiago', 1),

    (12, 8, 'Av. Kennedy', '5600',
        'Vitacura', 'Santiago', 1),

    (13, 8, 'Calle Condell', '745',
        'Providencia', 'Santiago', 1),

    (14, 9, 'Av. España', '1025',
        'Centro', 'Concepción', 1),

    (15, 10, 'Calle San Diego', '910',
        'Santiago Centro', 'Santiago', 0);


-- ============================================================
-- 5. CARRITOS
-- ============================================================

INSERT INTO CARRITOS
    (id_carrito, id_cliente, fecha_creacion, habilitado)
VALUES
    (1, 1, '2026-01-02', 1),
    (2, 2, '2026-02-03', 1),
    (3, 3, '2026-03-01', 1),
    (4, 4, '2026-03-15', 1),
    (5, 5, '2026-04-02', 1),
    (6, 6, '2026-04-10', 0),
    (7, 7, '2026-05-01', 1),
    (8, 8, '2026-05-05', 1),
    (9, 9, '2026-06-01', 1),
    (10, 10, '2026-06-10', 0);


-- ============================================================
-- 6. ITEMS DE CARRITO
-- ============================================================

INSERT INTO ITEM_CARRITOS
    (id_item_carrito, id_carrito, id_producto, cantidad,
     precio_unitario, habilitado)
VALUES
    (1, 1, 3, 1, 329990.00, 1),
    (2, 1, 4, 1, 39990.00, 1),

    (3, 2, 5, 2, 49990.00, 1),
    (4, 2, 16, 1, 24990.00, 1),

    (5, 3, 14, 1, 249990.00, 1),

    -- Carrito vacío: id_carrito = 4

    (6, 5, 9, 1, 79990.00, 1),
    (7, 5, 11, 2, 45990.00, 1),

    -- Carrito y producto inhabilitados
    (8, 6, 18, 1, 59990.00, 0),

    (9, 7, 7, 1, 179990.00, 1),
    (10, 7, 8, 1, 129990.00, 1),

    (11, 8, 13, 1, 399990.00, 1);

    -- Carritos 9 y 10 sin productos.


-- ============================================================
-- 7. PEDIDOS
-- ============================================================
-- Estados:
-- 1 CREADO
-- 2 CONFIRMADO
-- 3 EN_PREPARACION
-- 4 ENVIADO
-- 5 ENTREGADO
-- 6 CANCELADO

INSERT INTO PEDIDOS
    (id_pedido, id_cliente, id_direccion_entrega, id_estado_pedido,
     fecha, total, habilitado)
VALUES
    (1, 1, 1, 5, '2026-01-10', 627960.00, 1),

    (2, 2, 3, 4, '2026-02-05', 899970.00, 1),

    (3, 3, 5, 3, '2026-03-08', 319980.00, 1),

    (4, 4, 6, 2, '2026-03-20', 424980.00, 1),

    (5, 5, 8, 1, '2026-04-04', 125980.00, 1),

    (6, 6, 9, 6, '2026-04-15', 429990.00, 0),

    (7, 7, 11, 5, '2026-05-03', 369960.00, 1),

    (8, 8, 12, 4, '2026-05-08', 239980.00, 1),

    (9, 9, 14, 5, '2026-05-15', 149980.00, 1),

    (10, 10, 15, 2, '2026-06-02', 299970.00, 1),

    (11, 1, 2, 5, '2026-06-12', 149970.00, 1),

    (12, 3, 5, 4, '2026-06-20', 145970.00, 1),

    (13, 4, 7, 2, '2026-07-02', 109980.00, 1),

    (14, 7, 11, 3, '2026-07-10', 579980.00, 1);


-- ============================================================
-- 8. DETALLE DE PEDIDOS
-- ============================================================
-- Los precios unitarios representan el precio al momento
-- de realizar la compra, por lo que pueden diferir del
-- precio actual del producto.

INSERT INTO DETALLE_PEDIDOS
    (id_detalle_pedido, id_pedido, id_producto, cantidad,
     precio_unitario, habilitado)
VALUES
    -- Pedido 1
    (1, 1, 1, 1, 549990.00, 1),
    (2, 1, 3, 1, 39990.00, 1),
    (3, 1, 4, 2, 18990.00, 1),

    -- Pedido 2
    (4, 2, 12, 1, 799990.00, 1),
    (5, 2, 5, 2, 49990.00, 1),

    -- Pedido 3
    (6, 3, 14, 1, 249990.00, 1),
    (7, 3, 17, 1, 69990.00, 1),

    -- Pedido 4
    (8, 4, 13, 1, 399990.00, 1),
    (9, 4, 16, 1, 24990.00, 1),

    -- Pedido 5
    (10, 5, 9, 1, 79990.00, 1),
    (11, 5, 11, 1, 45990.00, 1),

    -- Pedido 6: cancelado
    (12, 6, 19, 1, 429990.00, 1),

    -- Pedido 7
    (13, 7, 7, 1, 179990.00, 1),
    (14, 7, 8, 1, 129990.00, 1),
    (15, 7, 22, 2, 29990.00, 1),

    -- Pedido 8
    (16, 8, 23, 1, 79990.00, 1),
    (17, 8, 24, 1, 159990.00, 1),

    -- Pedido 9
    (18, 9, 15, 1, 89990.00, 1),
    (19, 9, 18, 1, 59990.00, 1),

    -- Pedido 10
    (20, 10, 2, 1, 189990.00, 1),
    (21, 10, 10, 1, 69990.00, 1),
    (22, 10, 20, 1, 39990.00, 1),

    -- Pedido 11
    (23, 11, 6, 2, 29990.00, 1),
    (24, 11, 21, 1, 89990.00, 1),

    -- Pedido 12
    (25, 12, 9, 1, 79990.00, 1),
    (26, 12, 11, 1, 45990.00, 1),
    (27, 12, 4, 1, 19990.00, 1),

    -- Pedido 13
    (28, 13, 18, 2, 54990.00, 1),

    -- Pedido 14
    (29, 14, 1, 1, 549990.00, 1),
    (30, 14, 6, 1, 29990.00, 1);


-- ============================================================
-- 9. PAGOS
-- ============================================================
-- Estados:
-- 1 PENDIENTE
-- 2 APROBADO
-- 3 RECHAZADO
-- 4 REEMBOLSADO
--
-- Algunos pedidos tienen más de un pago para representar
-- intentos de pago o posteriormente un reembolso.

INSERT INTO PAGOS
    (id_pago, id_pedido, id_estado_pago, monto, fecha, metodo_pago, habilitado)
VALUES
    (1, 1, 2, 627960.00,
        '2026-01-10 15:30:00', 'Tarjeta de crédito', 1),

    (2, 2, 2, 899970.00,
        '2026-02-05 12:10:00', 'Transferencia bancaria', 1),

    (3, 3, 1, 319980.00,
        '2026-03-08 19:20:00', 'Webpay', 1),

    (4, 4, 3, 424980.00,
        '2026-03-20 09:15:00', 'Tarjeta de débito', 0),

    (5, 4, 2, 424980.00,
        '2026-03-20 09:22:00', 'Tarjeta de débito', 1),

    (6, 5, 1, 125980.00,
        '2026-04-04 21:05:00', 'Transferencia bancaria', 1),

    (7, 6, 3, 429990.00,
        '2026-04-15 10:40:00', 'Mercado Pago', 1),

    (8, 7, 2, 369960.00,
        '2026-05-03 13:50:00', 'Tarjeta de crédito', 1),

    (9, 8, 2, 239980.00,
        '2026-05-08 17:30:00', 'Transferencia bancaria', 1),

    (10, 9, 2, 149980.00,
        '2026-05-15 11:00:00', 'Webpay', 1),

    (11, 9, 4, 149980.00,
        '2026-05-20 14:30:00', 'Webpay', 1),

    (12, 10, 2, 299970.00,
        '2026-06-02 18:45:00', 'Tarjeta de débito', 1),

    (13, 11, 2, 149970.00,
        '2026-06-12 16:25:00', 'Tarjeta de crédito', 1),

    (14, 11, 4, 149970.00,
        '2026-06-18 10:15:00', 'Tarjeta de crédito', 1),

    (15, 12, 2, 145970.00,
        '2026-06-20 20:00:00', 'Webpay', 1),

    (16, 13, 1, 109980.00,
        '2026-07-02 09:30:00', 'Transferencia bancaria', 1),

    (17, 14, 1, 579980.00,
        '2026-07-10 11:45:00', 'Tarjeta de crédito', 1);


-- ============================================================
-- 10. ENVIOS
-- ============================================================
-- Se incluyen envíos entregados, enviados, uno aún sin despacho
-- y uno inhabilitado asociado a un pedido cancelado.

INSERT INTO ENVIOS
    (id_envio, id_pedido, fecha_despacho,
     fecha_entrega_estimada, fecha_entrega_real,
     numero_seguimiento, transportista, habilitado)
VALUES
    (1, 1,
        '2026-01-11',
        '2026-01-14',
        '2026-01-13',
        'STGO-2026-000001',
        'Chilexpress',
        1),

    (2, 2,
        '2026-02-06',
        '2026-02-09',
        NULL,
        'STGO-2026-000002',
        'Blue Express',
        1),

    (3, 6,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        0),

    (4, 7,
        '2026-05-04',
        '2026-05-07',
        '2026-05-06',
        'STGO-2026-000004',
        'CorreosChile',
        1),

    (5, 8,
        '2026-05-09',
        '2026-05-12',
        NULL,
        'STGO-2026-000005',
        'Blue Express',
        1),

    (6, 9,
        '2026-05-16',
        '2026-05-19',
        '2026-05-18',
        'CCP-2026-000006',
        'Chilexpress',
        1),

    (7, 11,
        '2026-06-13',
        '2026-06-16',
        '2026-06-15',
        'STGO-2026-000007',
        'Starken',
        1),

    (8, 12,
        '2026-06-21',
        '2026-06-24',
        NULL,
        'STGO-2026-000008',
        'CorreosChile',
        1),

    -- Pedido confirmado, aún sin despacho:
    -- sirve para probar campos NULL.
    (9, 13,
        NULL,
        '2026-07-08',
        NULL,
        NULL,
        'Chilexpress',
        1),

    -- Pedido en preparación con información de despacho aún pendiente.
    (10, 14,
        NULL,
        '2026-07-17',
        NULL,
        NULL,
        NULL,
        1);