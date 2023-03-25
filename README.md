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

una vez q probe todo migre y se q esta bien voy a hacer un
git add .

y despues le hago un git commit -m "un mensaje"

* una vez q ya esta el commit voy a tener que hacer un
git push , como es un clon n es necesario poner el git -m
con este git push se guarda todo en el repositorio de git hub.

* Vamos a modificar o agregar la url de nuestro proyecto django para eso
entramos a la carpeta proyecto django ---<>urls.py , y dentro de la misma al diccionario urlpattern , con la palabra reservada path creamos nuestra nueva url.

* Para hacerlo mejor cree una carpeta views.py y dentro una funcion
def mi_vista(request):
return ..

*Dentro del archivo views , necesito importar datos de la libreria de django , para eso utilizo 
from django.http import HttpResponse

*una vez importado nuestra funcion mi_vista podemos completarla con etiquetas str(strings)

* ejemplo de etiquetea <h1 ></h1> se usa para resaltar texto