from django.db import models
from EconomyManager.apps.usuario.models import Usuario

class Base(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Propietario")

    class Meta:
        abstract = True
