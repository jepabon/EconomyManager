from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy

class Usuario(AbstractUser):

    detail_view = 'usuario:detalle'
    edit_view = 'usuario:edicion'
    delete_view = 'usuario:eliminacion'

    @property
    def get_detail_url(self):
        return reverse_lazy(self.detail_view,args=[str(self.id)])
    @property
    def get_edit_url(self):
        return reverse_lazy(self.edit_view,args=[str(self.id)])
    @property
    def get_delete_url(self):
        return reverse_lazy(self.delete_view,args=[str(self.id)])