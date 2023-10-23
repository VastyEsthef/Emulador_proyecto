from django.db import models
from django.contrib.auth.models import User

class Cmaquinas_virtuales(models.Model):
   usuario = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               null=True, 
                               blank=True)
   
   nombre = models.CharField(max_length=100)

   sistema_operativo = models.CharField(max_length=100)

   sabor = models.CharField(max_length=200)

   tipo = models.CharField(max_length=50)

   descripcion = models.TextField(null=True, 
                               blank=True)

   creado = models.DateTimeField(auto_now_add=True)

   estado = models.BooleanField(default=False)

   def __str__(self):
      return self.nombre
   
