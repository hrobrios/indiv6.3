from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre=models.CharField(max_length=20)
    url=models.URLField()


def __str__(self):
    return self.nombre
    
def __str__(self):   
    return self.url