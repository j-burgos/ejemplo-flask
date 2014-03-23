Ejemplo básico con Flask y SQLAlchemy
=====================================

Esta aplicación genera una lista de nombres de personas
Y existe la posibilidad de agregar nuevos nombres a la lista

Este es un ejemplo muy básico para mostrar los conceptos básicos de Flask
Se utilizan:

- Rutas con y sin párametros
- Generación de respuestas con templates
- Templates que reciben parametros
- Tomar parametros de un request mediante post
- Manejo de errores como 404 y 500
- Un modelo básico de SQLAlchemy
- Listar y agregar objetos en la base de datos

Se utilizó para una sesión de ~3 horas de un taller de desarrollo con Python

Instalación
===========

Se debe crear un virtual environment, activarlo y luego instalar las dependencias

	virtualenv venv
	venv\Scripts\activate.bat (Windows)
	. venv/bin/activate (Linux/mac)
	pip install -r requirements.txt
