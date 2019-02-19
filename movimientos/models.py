from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Movimiento(models.Model):

    CATEGORIA_CHOICES = (
        ("gastos", "Gastos"),
        ("diversion", "Diversión"),
        ("ahorro", "Ahorro"),
    )

    SUBCATEGORIA_CHOICES = (
        ("", ""),
        ("", ""),
        ("", ""),
    )

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    fecha = models.DateTimeField(null=False, blank=False, default=datetime.now, verbose_name="Fecha")
    valor = models.FloatField(null=False, blank=False, default=0, verbose_name="Valor")
    categoria = models.CharField(max_length=255, default="gastos", choices=CATEGORIA_CHOICES,verbose_name="Categoría")
    subcategoria = models.CharField(max_length=255, default="gastos", choices=SUBCATEGORIA_CHOICES,verbose_name="Categoría")
    descripcion = models.TextField(null=False, blank=False, default="", verbose_name="Descripción")

    def __str__(self):
        return str(self.id)
