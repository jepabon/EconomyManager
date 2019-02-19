from django.urls import path
from .views import reporte_gastos

urlpatterns = [
    path('', reporte_gastos)
]