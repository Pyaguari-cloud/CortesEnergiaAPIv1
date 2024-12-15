from django.db import models

# Create your models here.
class Sector(models.Model):
    nombre = models.CharField(max_length=100)
    hora_inicio = models.TimeField() # formato de 24 horas
    hora_fin = models.TimeField() # formato de 24 horas
    poligono_coordenadas = models.TextField() # lista de coordenadas (puede ser json o texto)


    def __str__(self):
        return self.nombre