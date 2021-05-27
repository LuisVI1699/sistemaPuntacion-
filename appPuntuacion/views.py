from django.shortcuts import render
from .models import Localidad
from json import dumps


# Create your views here.

def puebla(request):
    Localidades = Localidad.objects.all()
    nombre= Localidades.nombre
    puntaje = Localidades.puntaje
    return render(request, 'appPuntuacion/puebla.html', {'Nombre': dumps(nombre), 'Puntaje':dumps(puntaje)})
