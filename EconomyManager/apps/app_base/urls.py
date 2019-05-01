from django.urls import path,include
from EconomyManager.apps.app_base.views import LoginView
    
app_name = 'app_base'

urlpatterns = [
    path('login', LoginView.as_view(), name='login')
]