from rest_framework import generics
from .models import Inventario, Stock
from .serializers import InventarioSerializer, StockSerializer

class InventarioListCreateView(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class InventarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
import pandas as pd
from .models import Inventario

class ExportarInventarioView(APIView):
    def get(self, request):
        data = Inventario.objects.all().values()
        df = pd.DataFrame(data)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="inventario.xlsx"'
        df.to_excel(response, index=False)
        return response