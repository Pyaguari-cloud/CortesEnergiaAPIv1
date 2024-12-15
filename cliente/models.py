from django.db import models
from usuario.models import Usuario
# Create your models here.
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='cliente', null=True, blank=True)
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo_electronico = models.EmailField(unique=True)
    coordenadas = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.nombres} {self.apellidos}"