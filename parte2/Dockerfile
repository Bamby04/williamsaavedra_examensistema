FROM python:3.11-slim


# Crear usuario no-root
RUN useradd --create-home appuser


WORKDIR /app


# Copiar primero requirements para aprovechar cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copiar el resto del código
COPY app.py ./


# Variable de entorno por defecto
ENV PORT=5000


EXPOSE 5000


# Cambiar a usuario no-root
USER appuser


CMD ["python", "app.py"]