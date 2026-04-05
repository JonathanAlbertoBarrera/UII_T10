# Equipo1 Almacen — API REST Productos

API REST construida con Django 4.2 y Django REST Framework. Permite gestionar un catálogo de productos con operaciones CRUD y un endpoint para descontar stock.

---

## Requisitos previos

Python 3.10 o superior
MySQL 8 corriendo localmente
pip

---

## 1. Clonar el repositorio

bash
git clone https://github.com/JonathanAlbertoBarrera/UII_T10.git
cd UII_T10/equipo1Almacen

---

## 2. Crear y activar entorno virtual

bash
python -m venv venv

**Windows CMD:**
cmd
venv\Scripts\activate

**Windows PowerShell:**
powershell
venv\Scripts\Activate.ps1

---

## 3. Instalar dependencias

bash
pip install -r requirements.txt

---

## 4. Configurar variables de entorno

Copia el archivo de ejemplo y rellena tus datos:

bash
copy .env.example .env

Edita .env con tus credenciales reales:

env
SECRET_KEY=django-insecure-pon-tu-clave-aqui
DEBUG=True
DB_NAME=nombre_de_tu_bd
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306

---

## 5. Crear la base de datos en MySQL

Conéctate a MySQL y ejecuta:

sql
CREATE DATABASE api_producto;

---

## 6. Ejecutar migraciones

bash
python manage.py makemigrations
python manage.py migrate

## 7. Levantar el servidor

bash
python manage.py runserver

La API queda disponible en: `http://localhost:8000/api/`  

---

## Endpoints

| Método | URL | Descripción |
|--------|-----|-------------|
| GET | /api/productos/ | Listar todos los productos |
| POST | /api/productos/ | Crear un producto |
| GET | /api/productos/{id}/ | Ver un producto |
| PUT | /api/productos/{id}/ | Actualizar completo |
| PATCH | /api/productos/{id}/ | Actualizar parcial |
| DELETE | /api/productos/{id}/ | Eliminar |
| POST | /api/productos/{id}/descontar_stock/ | Descontar stock |

### Ejemplo — Crear producto

json
{
  "nombre": "Laptop",
  "descripcion": "Laptop gaming",
  "precio": "15999.99",
  "stock": 10
}

### Ejemplo — Descontar stock

json
{
  "cantidad": 3
}

---

## Archivos importantes

| Archivo | Descripción |
|---------|-------------|
| .env | Variables de entorno reales (no se sube a git) |
| equipo1Almacen/.env.example | Plantilla de variables de entorno |
| equipo1Almacen/equipo1Almacen/settings.example.py | Plantilla del settings con todas las configuraciones |

## Documentación con Swagger

El proyecto cuenta con documentación interactiva generada con Swagger, lo que permite probar los endpoints directamente desde el navegador

Una vez levantado el servidor, puedes acceder a:
---
Swagger UI: http://localhost:8000/swagger/
---
