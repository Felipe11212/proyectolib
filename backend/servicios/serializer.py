from rest_framework import serializers
from .models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    valor = serializers.SerializerMethodField()

    class Meta:
        model = Servicio
        fields = ['id', 'placa', 'hora_entrada', 'hora_salida', 'valor']

    def get_valor(self, obj):
        return obj.calcular_valor()
