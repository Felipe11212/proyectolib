from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=60)
    stock = models.IntegerField()
    precio = models.FloatField()
    fecha_vencimiento = models.DateTimeField()
    fecha_fabricacion = models.DateTimeField()


    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cantidad_producto = models.IntegerField()
    fecha_venta = models.DateTimeField()
    total_precio = models.FloatField()
    Producto = models.CharField(max_length=80, default='Sin categoria')
    def __str__(self):
         return f'Venta de {self.cantidad_producto} de {self.producto.nombre}'
     
