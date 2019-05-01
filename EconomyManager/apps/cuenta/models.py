from django.db import models
from EconomyManager.apps.app_base.models import Base
from EconomyManager.apps.categoria_cuenta.models import CategoriaCuenta

class Cuenta(Base):
    nombre = models.CharField(max_length=50, blank=False, null=True, verbose_name="Nombre")
    balance = models.FloatField(blank=False, null=True, verbose_name="Balance")
    categoria_cuenta = models.ForeignKey(CategoriaCuenta, on_delete=models.CASCADE, verbose_name="Categoria Cuenta")
