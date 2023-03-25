from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("<h1>Mi Primera Vista</h1>")