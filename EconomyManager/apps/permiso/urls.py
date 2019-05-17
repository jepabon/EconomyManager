from django.urls import path,include
from EconomyManager.apps.permiso.views import PermisoIndexView

app_name = 'permiso'

urlpatterns = [
    path('',PermisoIndexView.as_view(),name='index')
]