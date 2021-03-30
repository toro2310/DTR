from django.db import models

# Create your models here.

class administracion(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)


class porteria(models.Model):
    id =  models.CharField(primary_key=True, max_length=200)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)



class residente(models.Model):
    id =  models.CharField(primary_key=True, max_length=200)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    num_apartamEnto = models.CharField(max_length=5)
    telefono = models.CharField(max_length=20)

