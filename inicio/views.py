from datetime import datetime
from django.http import HttpResponse
from django.template import Template , Context , loader
from inicio.models import Animal


def mi_vista(request):
    return HttpResponse("<h1>Mi Primera Vista ahora mismo</h1>")

#VERSION CON HttpResponse
# def mostrar_fecha(request):
#     return HttpResponse(f"<p>{datetime.now()}</p>")

def saludar(request,nombre,apellido):
    return HttpResponse(f"<h1>Hola {nombre}{apellido}</h1>")

def mi_primer_template(request):
    
    archivo = open(r"C:\Users\poolm\Desktop\PROGRAMACION\PYTHON\proyecto_django\Proyecto_django\template\mi_primer_template.html", "r")
    # archivo = open(r"mi_primer_template.html", "r")
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

#VERSION CON TEMPLATE

def mostrar_fecha(request):
    dt = datetime.now()
    
    dt_formateado = dt.strftime("%A %d %B %Y %I %M")
    
    # archivo = open(r"C:\Users\poolm\Desktop\PROGRAMACION\PYTHON\proyecto_django\Proyecto_django\template\mi_primer_template.html", "r")
    
    # archivo = open(r"mostrar_fecha.html", "r")
    # template = Template(archivo.read())
    # archivo.close()
    template = loader.get_template(r"mostrar_fecha.html")
    
    # contexto = Context({"fecha" : dt_formateado})
    # template_renderizado = template.render(contexto)
    
    
    template_renderizado = template.render({"fecha" : dt_formateado})
    
    return HttpResponse(template_renderizado)
    
def prueba_template(request):
    
     datos = {
         "nombre" : "pepito",
         "apellido" : "grillo",
         "edad" : 16,
         "anios" : [1995 ,2004 ,2014 ,2017 ,2021,2022]
     }
    
     template = loader.get_template(r"prueba_template.html")
    
     template_renderizado = template.render(datos)
    
     return HttpResponse(template_renderizado)
 
 
 
def crear_animal(request):
    
    animal = Animal(nombre ="ricardo" , edad =3)
    print(animal.nombre)
    print(animal.edad)
    animal.save()
    
    datos ={"animal" : animal}
    template = loader.get_template(r"crear_animal.html")
    
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)
     
    
    
    
  
