# App Tienda — Sistema de gestión de tienda virtual

## Integrantes

- Felipe Rodriguez
- Emmanuel Molinet

## Descripción general

Aplicación de consola para la gestión de una tienda virtual. Administra categorías, productos, clientes,
direcciones de entrega, pedidos, pagos, envíos, carritos de compra y usuarios del sistema.

La persistencia se realiza en MySQL mediante el ORM **Peewee**. Las contraseñas de los usuarios se
almacenan como hash con **BCrypt** y se ocultan al escribirlas con **Maskpass**.

El proyecto sigue una arquitectura por capas:

```
AP_N2_C2_POO-APP-tienda-online-main/
├── datos/            # Persistencia: conexión, modelos ORM, repositorios y scripts SQL
│   ├── conexion.py
│   ├── Modelos/
│   ├── repositorios/
│   └── sql/
├── negocio/          # Reglas de negocio y validaciones de procesos
├── presentacion/     # Menús, captura de datos y presentación de resultados
├── auxiliares/       # Mensajes, menús, validaciones y configuración de la aplicación
├── diagrama UML apptienda.png
├── requirements.txt
├── .env              # Credenciales de conexión a la base de datos
└── main.py            # Punto de entrada
```

## Dependencias

Requisitos del sistema:

- Python 3.10 o superior
- MySQL 8.0 o superior

Librerías de Python (se instalan con `requirements.txt`):

| Librería | Uso |
|---|---|
| peewee | ORM para la persistencia |
| PyMySQL | Driver de conexión a MySQL |
| python-decouple | Lectura de credenciales desde `.env` |
| bcrypt | Hash de contraseñas |
| maskpass | Ocultar la contraseña al escribirla |
| prettytable | Tablas en la consola |
| wcwidth | Dependencia de prettytable |

## Procedimiento de instalación

1. Clonar el repositorio y entrar a la carpeta del proyecto.

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # Linux / macOS
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configurar la conexión en el archivo `.env` de la raíz. Si tu MySQL local usa otro usuario o
   contraseña, edítalo antes de ejecutar:

   ```
   db=apptienda
   host='localhost'
   port=3306
   user='glast_app'
   password='tu_contrasena'
   ```

5. Crear en MySQL el usuario de la aplicación (debe coincidir con el `.env`):

   ```sql
   CREATE USER 'glast_app'@'localhost' IDENTIFIED BY 'tu_contrasena';
   GRANT ALL PRIVILEGES ON apptienda.* TO 'glast_app'@'localhost';
   FLUSH PRIVILEGES;
   ```

## Procedimiento de creación de la base de datos

Los scripts están en la carpeta `datos/sql/`. Deben ejecutarse **en este orden**:

| Orden | Script | Qué hace |
|---|---|---|
| 1 | `datos/sql/creación base de datos.sql` | Crea la base `APPTIENDA` y las tablas del negocio |
| 2 | `datos/sql/inserción datos base de datos.sql` | Inserta datos de ejemplo (categorías, productos, clientes, etc.) |
| 3 | `datos/sql/datos/sql/2026.11.14_USUARIOS_Y_ROLES.sql` | Crea la tabla `usuarios` |
| 4 | `datos/sql/datos/sql/2026.11.23_USUARIO_INICIAL.sql` | Inserta el usuario administrador inicial |

Desde la terminal, con un usuario de MySQL con permisos para crear bases de datos:

```bash
mysql -u root -p < "datos/sql/creación base de datos.sql"
mysql -u root -p < "datos/sql/inserción datos base de datos.sql"
mysql -u root -p < "datos/sql/datos/sql/2026.11.14_USUARIOS_Y_ROLES.sql"
mysql -u root -p < "datos/sql/datos/sql/2026.11.23_USUARIO_INICIAL.sql"
```

También se pueden abrir y ejecutar en orden desde MySQL Workbench.

> **Advertencia:** el script del paso 3 elimina y vuelve a crear la tabla `usuarios`
> (`DROP TABLE IF EXISTS`). Si se vuelve a ejecutar, se pierden los usuarios existentes y hay que
> ejecutar de nuevo el paso 4.

## Usuario inicial

El script del paso 4 crea un administrador para poder iniciar sesión:

| Campo | Valor |
|---|---|
| Correo | `admin@apptienda.cl` |
| Contraseña | `Admin123!` |

La contraseña se guarda como hash BCrypt, no en texto plano. Se recomienda cambiarla después del
primer ingreso.

## Instrucciones de ejecución

Con el entorno virtual activado y la base de datos creada, ejecutar desde la raíz del proyecto:

```bash
python app.py
```

Se mostrará el menú principal. Para iniciar sesión, ir a **[9] Gestión Usuarios → [5] Iniciar sesión**
e ingresar el correo y la contraseña del usuario inicial (la contraseña se muestra como `*` al escribirla).
Desde ese mismo submenú se pueden crear, listar, modificar y deshabilitar usuarios.

Reglas para las contraseñas de nuevos usuarios: mínimo 8 caracteres, con al menos una mayúscula, una
minúscula, un número y un carácter especial (`@ $ # ! * &`).
