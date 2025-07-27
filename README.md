# 🛒 API de Supermercado + Extractor de Archivos (PDF/Excel/CSV)

Este proyecto es una API construida con Django REST Framework. Incluye autenticación JWT, manejo de usuarios, un CRUD de productos de supermercado y un sistema para extraer datos automáticamente de archivos (`.pdf`, `.csv`, `.xlsx`).

---

## 🚀 Características

- Login y autenticación con JWT
- CRUD de objetos de supermercado
- Extracción de pares clave-valor automáticamente de archivos PDF/CSV/Excel(e.g., `CURP: XXXXX`, `RFC: YYYYY`)
- Gestión de usuarios (ver y modificar perfil)
- Desplegable vía Docker en Azure App Service
- Uso de base de datos PostgreSQL
- Variables de entorno con `.env`

---

## ⚙️ Requisitos

- Python 3.11+
- Docker
- PostgreSQL
- Cuenta en Azure (para despliegue)

---

## 🧪 Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo
```
2. Crea un entorno virtual y activa:

```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Crea el archivo .env:

```bash
cp .env.example .env
```

5. Ejecuta migraciones y levanta el servidor:

```bash
python manage.py migrate
python manage.py runserver
```
## 📦 Uso con Docker

Construcción de la imagen
```bash
docker build -t django-api .
```
Ejecución con Docker
```bash
docker run -p 8000:8000 --env-file .env django-api
```

## ☁️ Despliegue en Azure App Service

1. Sube tu código a GitHub.

2. En Azure Portal:

Crea un recurso App Service.

Crea un recurso Base de Datos PostgreSQL.

Ve a App Service > Configuration > Application Settings y define las variables del .env ahí (e.g. SECRET_KEY, DEBUG, DATABASE_URL, etc.).

Configura el despliegue desde tu repo GitHub o sube tu imagen Docker personalizada.

3. Asegúrate de que tu contenedor escuche en el puerto 8000.

## 🗂️ Estructura del proyecto

myproject/
├── file_manager/
├── manage.py
├── myproject/
│   └── settings.py
├── users/
├── items/
├── requirements.txt
├── .env.example
├── Dockerfile
└── README.md

## 📝 Variables de entorno esperadas
Consulta .env.example para conocer las variables necesarias. Por ejemplo:

```ini
SECRET_KEY=tu_clave
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://usuario:clave@localhost:5432/tu_db
```

## 🧠 Autor
💻 José Ángel Robles Otero 

## ⚖️ Licencia
Este proyecto es de uso académico o técnico. Puedes adaptarlo y reutilizarlo según necesidades.