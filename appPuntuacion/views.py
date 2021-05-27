from django.shortcuts import render
from .models import Localidad
from json import dumps


# Create your views here.

def localidades(request):
    Localidades=Localidad.objects.all()
    nombre=[]
    puntuacion=[]
    for localidad in Localidades:
        nombre.append(localidad.nombre)
        puntuacion.append(localidad.puntuacion)
    return render(request, 'appPuntuacion/localidades.html', {'Nombre':dumps(nombre), 'Puntuacion':dumps(puntuacion)})
