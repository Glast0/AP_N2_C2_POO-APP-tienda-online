# Sistema de gestión de tienda virtual.
Sistema de gestión de una tienda virtual. Administra categorías, productos, clientes, direcciones,
pedidos, pagos, y la creación de carritos. Conectado a MySQL mediante ORM peewee.

Requisitos
Pyhton 3.10 o superior
MySQL 8.0 o superior

Instalación

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

El archivo .env de la raíz contiene las credenciales de conexión. Si tu MySQL local usa otro usuario o contraseña, edítalo antes de ejecutar:

db=apptienda
host='localhost'
port=3306
user='glast'
password='tu_contrasena'

El usuario debe existir en tu MySQL local y coincidir con el .env:

CREATE USER 'glast'@'localhost' IDENTIFIED BY 'tu_contrasena';
GRANT ALL PRIVILEGES ON sistema_pyme.* TO 'glast'@'localhost';
FLUSH PRIVILEGES;

Scripts SQL
Se deben ejecutar los scripts SQL de la raíz en este orden:

creación base de datos.sql
inserción datos base de datos.sql

Ejecución de la terminal de gestión:

python app.py