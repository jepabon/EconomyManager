from django.urls import path,include
from EconomyManager.apps.usuario.views import LoginView
    

app_name = 'usuario'

urlpatterns = [
    path('login', LoginView.as_view(), name='login')
]