from django.db import models
from django.utils import timezone

class Servicio(models.Model):
    placa = models.CharField(max_length=10)
    hora_entrada = models.DateTimeField(default=timezone.now)
    hora_salida = models.DateTimeField(null=True, blank=True)

    def calcular_valor(self):
        import numpy as np
        if not self.hora_salida:
            return 0
        tiempo = self.hora_salida - self.hora_entrada
        horas = np.ceil(tiempo.total_seconds() / 3600) 
        return int(horas * 2000)

    def __str__(self):
        return f"{self.placa} - ${self.calcular_valor()}"
