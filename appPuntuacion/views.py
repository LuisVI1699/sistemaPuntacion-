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
    LocalidadSelect=request.GET.get('localidad')
    local=Localidad.objects.get(nombre__icontains=LocalidadSelect)
    nombreLocalidad= local.nombre
    puntuacionLocalidad=local.puntuacion
    return render(request, 'appPuntuacion/localidadSelect.html', {'NombreLocalidad':nombreLocalidad, 'PuntuacionLocalidad':dumps(puntuacionLocalidad)})