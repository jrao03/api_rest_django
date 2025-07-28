# Imagen oficial de Python
FROM python:3.11-slim

# Crea y usa directorio en el contenedor
WORKDIR /app

# Copia las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . .

# Copia el script de inicio y le da permisos de ejecución
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expone el puerto 8000 para gunicorn
EXPOSE 8000

# Usa el script de inicio como comando principal
CMD ["/app/entrypoint.sh"]