# Imagen oficial de Python
FROM python:3.11-slim

# Crea y usa directorio en el contenedor
WORKDIR /app

# Copia dependencias y el proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto 8000 para gunicorn
EXPOSE 8000

# Comando para iniciar con gunicorn
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
