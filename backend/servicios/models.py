from django.db import models
from django.utils import timezone

class Servicio(models.Model):
    placa = models.CharField(max_length=10)
    hora_entrada = models.DateTimeField(default=timezone.now)
    hora_salida = models.DateTimeField(null=True, blank=True)

# numpy
def calcular_valor(self):
    import numpy as np  # Importamos NumPy para usar funciones matemáticas como np.ceil

    # Si no hay hora de salida registrada, el vehículo aún no ha salido
    if not self.hora_salida:
        return 0  # No se cobra nada si no ha salido

    # Calculamos la diferencia de tiempo entre entrada y salida
    tiempo = self.hora_salida - self.hora_entrada

    # Convertimos esa diferencia a segundos, luego a horas (dividido por 3600)
    # y usamos np.ceil para redondear hacia arriba al número entero de horas
    horas = np.ceil(tiempo.total_seconds() / 3600)

    # Multiplicamos las horas por 2000 (valor por hora) y convertimos a entero
    return int(horas * 2000)

# Este método define cómo se mostrará el objeto al imprimirlo (ej. print(objeto))
def __str__(self):
    # ///////////////////////////////////////////////


    
    # Devuelve una cadena con la placa y el valor calculado
    return f"{self.placa} - ${self.calcular_valor()}"
