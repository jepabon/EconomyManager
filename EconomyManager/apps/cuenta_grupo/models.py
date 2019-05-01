from django.db import models
from EconomyManager.apps.app_base.models import Base
from EconomyManager.apps.cuenta.models import Cuenta
from EconomyManager.apps.grupo.models import Grupo

class CuentaGrupo(Base):
    valor = models.FloatField(blank=False, null=True, verbose_name="Valor")
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name="Cuenta")
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name="Grupo")

