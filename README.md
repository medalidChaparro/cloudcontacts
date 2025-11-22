CloudContacts

CloudContacts es una aplicación web desarrollada con Flask, MySQL y Gunicorn, diseñada para gestionar contactos de manera sencilla, segura y accesible desde cualquier lugar. El proyecto incluye autenticación de usuarios, almacenamiento en base de datos, despliegue en AWS EC2 y una arquitectura optimizada para producción.

🚀 Características principales

Registro e inicio de sesión con contraseñas encriptadas.

Gestión completa de contactos (crear, listar y eliminar).

Conexión a una base de datos MySQL en AWS RDS.

Aplicación desplegada en un servidor Ubuntu con Gunicorn y Systemd.

Acceso público mediante la IP del servidor: http://3.93.170.228

📁 Estructura del proyecto
cloudcontacts/
├── app.py
├── database.py
├── requirements.txt
├── venv/
├── static/
├── templates/
└── README.md

🛠️ Tecnologías utilizadas

Python 3

Flask

MySQL (AWS RDS)

Gunicorn

Systemd

Ubuntu Server en AWS EC2

HTML + CSS

⚙️ Instalación local

Clonar el repositorio:

git clone https://github.com/medalidChaparro/cloudcontacts.git
cd cloudcontacts


Crear un entorno virtual:

python3 -m venv venv
source venv/bin/activate


Instalar dependencias:

pip install -r requirements.txt


Crear el archivo .env con las variables:

DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=
SECRET_KEY=


Ejecutar la aplicación:

python3 app.py

🌐 Acceso en la nube (Producción)

La aplicación está desplegada en un servidor AWS EC2 y disponible en:

http://3.93.170.228

🏗️ Despliegue en AWS (resumen)

Se configuró una instancia EC2 con Ubuntu.

Se instaló Python, virtualenv y Git.

Se clonó el repositorio y se activó el entorno virtual.

Se instaló Gunicorn como servidor WSGI.

Se creó un servicio Systemd para ejecución automática.

Se abrió el puerto 5000 en el Security Group.

🔐 Seguridad

Contraseñas almacenadas con hashing mediante Werkzeug.

Comunicación con RDS mediante credenciales protegidas.

Uso de variables de entorno con .env.

Gunicorn corriendo como servicio de systemd.

📸 Vista general

Aplicación accesible públicamente desde:

http://3.93.170.228

📌 Autor

Proyecto desarrollado por Medalid Chaparro.
