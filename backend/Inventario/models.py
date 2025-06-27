from django.db import models

# Esta clase representa el inventario con la fecha que se realizó.
class Inventario(models.Model):
    fecha_inventario = models.DateField()
    producto = models.CharField(max_length=80, default='Sin categoría')
    stock = models.CharField(max_length=80, default='Sin categoría')
    comentario = models.CharField(max_length=80, default='Sin categoría')

    def __str__(self):
        return f'Inventario de {self.producto}'
    

# Esta clase sirve para registrar cuántas unidades de un producto hay en un inventario determinado.
class Stock(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, related_name='stocks')  # ✅ relación
    cantidad_stock = models.IntegerField()
    nombre_producto = models.CharField(max_length=100, default='Sin categoría')
    categoria = models.CharField(max_length=50, default='Sin categoría')

    def __str__(self):
        return f'{self.nombre_producto}: {self.cantidad_stock} unidades'
