from django.shortcuts import render
from .models import Localidad
from django.db.models import Max
from json import dumps


# Create your views here.
def localidades(request):
    Localidades=Localidad.objects.order_by('nombre')
    nombre=[]
    puntuacion=[]
    for localidad in Localidades:
        nombre.append(localidad.nombre)
        puntuacion.append(localidad.puntuacion)
    maxPuntuacion=Localidad.objects.all().aggregate(Max('puntuacion'))
    return render(request, 'appPuntuacion/localidades.html', {'todo':Localidades,'Nombre':dumps(nombre), 'Puntuacion':dumps(puntuacion), 'MaxPuntuacion':maxPuntuacion["puntuacion__max"]})

def localidadSelect(request,localidad_id):
    info=Localidad.objects.get(id=localidad_id)
    Localidades=Localidad.objects.order_by('nombre')
    nombre=[]
    puntuacion=[]
    for localidad in Localidades:
        nombre.append(localidad.nombre)
        puntuacion.append(localidad.puntuacion)
    maxPuntuacion=Localidad.objects.all().aggregate(Max('puntuacion'))
    LocalidadSelect=Localidad.objects.get(id=localidad_id)
    #LocalidadSelect=request.GET.get('localidad')
    local=Localidad.objects.get(nombre__icontains=LocalidadSelect)
    nombreLocalidad= local.nombre
    puntuacionLocalidad=local.puntuacion
    return render(request, 'appPuntuacion/localidadSelect.html', {'INFO':info,'Nombre':dumps(nombre), 'Puntuacion':dumps(puntuacion),'NombreLocalidad':nombreLocalidad, 'PuntuacionLocalidad':dumps(puntuacionLocalidad), 'MaxPuntuacion':dumps(maxPuntuacion["puntuacion__max"])})

