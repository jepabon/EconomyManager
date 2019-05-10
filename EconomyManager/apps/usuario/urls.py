from django.urls import path,include
from EconomyManager.apps.usuario.views import UsuarioCreacionView,UsuarioEdicionView,UsuarioIndexView

app_name = 'usuario'

urlpatterns = [
    path('',UsuarioIndexView.as_view(),name='index'),
    path('creacion',UsuarioCreacionView.as_view(),name='creacion'),
    path('edicion/<int:pk>',UsuarioEdicionView.as_view(),name='edicion')
]