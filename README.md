# Proyecto_django

*- Creamos nuestro proyecto django , primero creamos un repositorio en git hub

*-Despues vamos a generar un entorno virtual 
python -m venv venv

*Despues instalamos nuestro paquete dnd esta django
pip install django

*genero el archivo requirements.txt para que queden acentados los paquetes que uso en mi proyecto

*inicializo mi proyecto django
django-admin startproject "nombre del proyecto"

Eso me va a crear una carpeta de django.

*Una vez creada debo iniciar mi proyecto django eso lo hago mediante el comando
python manage.py runserver

*Eso me va a crear una base de datos que la vamos a ver como  db.sqlite3 , la cual va a estar en 0 , 
necesitamos que esta base tenga los arvhivos necesarios para ejecutarse para eso , tenemos que migrar 
los datos de nuestro servidor , y lo hacemos con el comando
python manage.py migrate

* Con esto ya tengo lo basico de mi proyecto DJANGO para poder iniciarlo.

