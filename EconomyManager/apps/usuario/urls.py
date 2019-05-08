from django.urls import path,include
from EconomyManager.apps.usuario.views import UsuarioCreacionView,UsuarioEdicionView

app_name = 'usuario'

urlpatterns = [
    path('creacion',UsuarioCreacionView.as_view(),name='creacion'),
    path('edicion/<int:pk>',UsuarioEdicionView.as_view(),name='edicion')
]