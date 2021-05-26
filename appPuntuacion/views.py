from django.shortcuts import render


# Create your views here.

def puebla(request):
    return render(request, 'appPuntuacion/puebla.html',)
