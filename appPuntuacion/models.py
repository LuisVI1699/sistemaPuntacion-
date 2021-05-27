from django.db import models

# Create your models here.
class Localidad(models.Model):

    nombre=models.CharField(max_length=30)
    puntuacion=models.IntegerField()
    def __str__(self):
        return self.nombre
