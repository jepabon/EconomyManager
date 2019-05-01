from django.db import models
from EconomyManager.apps.app_base.models import Base

class CategoriaCuenta(Base):
    tipo = models.CharField(max_length=20, blank=False, null=True, verbose_name="Tipo")
    naturaleza = models.CharField(max_length=20, blank=False, null=True, verbose_name="Naturaleza")
    nombre = models.CharField(max_length=20, blank=False, null=True, verbose_name="Nombre")
