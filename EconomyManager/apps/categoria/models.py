from django.db import models
from EconomyManager.apps.app_base.models import Base
from EconomyManager.apps.grupo.models import Grupo

class Categoria(Base):
    nombre = models.CharField(max_length=50, blank=False, null=True, verbose_name="Nombre")
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name="Grupo")
