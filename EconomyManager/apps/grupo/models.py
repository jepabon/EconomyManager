from django.db import models
from EconomyManager.apps.app_base.models import Base

class Grupo(Base):
    nombre = models.CharField(max_length=50, blank=False, null=True, verbose_name="Nombre")
