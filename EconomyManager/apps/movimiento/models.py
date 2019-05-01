from django.db import models
from EconomyManager.apps.app_base.models import Base
from EconomyManager.apps.cuenta.models import Cuenta
from EconomyManager.apps.categoria.models import Categoria

class Movimiento(Base):
    fecha = models.DateTimeField(blank=False, null=True, verbose_name="Fecha")
    monto = models.FloatField(blank=False, null=True, verbose_name="Monto")
    naturaleza = models.BooleanField(default=1, blank=False, null=False, verbose_name="Naturaleza")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name="Cuenta")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
