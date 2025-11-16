# Examen Docker – Williams Saavedra

Este repositorio contiene las tres partes del examen: CLI, Dockerfile/Flask y Compose.

## Parte 1 – CLI y Contenedores

- Directorio: `parte1/`
- Contiene: `comandos.txt` con los comandos ejecutados y salidas
- Requisitos: Docker instalado
- Cómo ejecutar: abrir PowerShell y ejecutar los comandos listados.

## Parte 2 – Aplicación Flask + Dockerfile

- Directorio: `parte2/`
- Contiene: `app.py`, `requirements.txt`, `Dockerfile`, `.dockerignore`, `comandos.txt`
- Cómo levantar:
  ```bash
  docker build -t examen-flask .
  docker run -d -p 5000:5000 --name flask-examen -e STUDENT_NAME="Williams Saavedra" examen-flask
  ```
