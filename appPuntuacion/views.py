from django.shortcuts import render
from .models import Localidad
from json import dumps


# Create your views here.

def localidades(request):
    return render(request, 'appPuntuacion/localidades.html')
