FROM python:3.8-alpine

ENV FLASK_APP=/www/app.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=5000

# Instalar herramientas de compilación y dependencias necesarias
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    libffi-dev \
    build-base \
    mariadb-dev \
    libstdc++

# Crear directorio de trabajo y copiar archivos
WORKDIR /www
COPY . .

# Actualizar pip e instalar dependencias Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Dar permisos de ejecución al script
RUN chmod +x /www/entrypoint.sh

# Exponer el puerto de Flask
EXPOSE 5000

# Ejecutar el script de arranque
ENTRYPOINT ["/www/entrypoint.sh"]
