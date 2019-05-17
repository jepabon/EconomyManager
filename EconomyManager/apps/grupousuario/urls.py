from django.urls import path,include
from EconomyManager.apps.grupousuario.views import GrupoUsuarioCreacionView, GrupoUsuarioEdicionView, GrupoUsuarioIndexView, GrupoUsuarioEliminacionView, GrupoUsuarioDetalleView

app_name = 'grupousuario'

urlpatterns = [
    path('',GrupoUsuarioIndexView.as_view(),name='index'),
    path('creacion',GrupoUsuarioCreacionView.as_view(),name='creacion'),
    path('edicion/<int:pk>',GrupoUsuarioEdicionView.as_view(),name='edicion'),
    path('detalle/<int:pk>',GrupoUsuarioDetalleView.as_view(),name='detalle'),
    path('eliminacion/<int:pk>',GrupoUsuarioEliminacionView.as_view(),name='eliminacion')
]