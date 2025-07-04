from django.urls import path
from .views import ServicioListCreateView, ServicioDetailView

urlpatterns = [
    path('', ServicioListCreateView.as_view(), name='servicio-list'),
    path('<int:pk>/', ServicioDetailView.as_view(), name='servicio-detail'),
]
