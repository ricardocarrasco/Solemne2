from __future__ import unicode_literals
from sorl.thumbnail import ImageField
from django.db import models

# Create your models here.


class Productos(models.Model):
    sku = models.CharField(max_length=100,unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    marca = models.ForeignKey(Brand, null=True)
    categoria = models.ForeignKey(Category, null=True)
    status = models.BooleanField()
    imagen = models.ImageField(upload_to='images/data',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku

class Categorias(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True,null=True)
    banner = models.ImageField(upload_to='images/banner_categories',blank=True,null=True)
    orden_de_la_categoria = models.IntegerField(default=0)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Marcas(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='images/brand',blank=True, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

# Create your models here.
