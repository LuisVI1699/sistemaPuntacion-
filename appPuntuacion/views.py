from django.shortcuts import render
from .models import Localidad
from json import dumps


# Create your views here.
def localidades(request):
    Localidades=Localidad.objects.order_by('-puntuacion')
    nombre=[]
    puntuacion=[]
    for localidad in Localidades:
        nombre.append(localidad.nombre)
        puntuacion.append(localidad.puntuacion)
    return render(request, 'appPuntuacion/localidades.html', {'Nombre':dumps(nombre), 'Puntuacion':dumps(puntuacion)})

def localidadSelect(request):
    Localidades=Localidad.objects.order_by('-puntuacion')
    nombre=[]
    puntuacion=[]
    i=0

    for localidad in Localidades:
        nombre.append(localidad.nombre)
        puntuacion.append(localidad.puntuacion)

    while request.GET.get('localidad') != nombre[i]:
        i += 1;
    nombreLocalidad= nombre[i]
    puntuacionLocalidad=puntuacion[i]
    return render(request, 'appPuntuacion/localidadSelect.html', {'NombreLocalidad':nombreLocalidad, 'PuntuacionLocalidad':puntuacionLocalidad})