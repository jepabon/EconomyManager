from django.forms import ModelForm
from EconomyManager.apps.app_base.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','first_name','last_name','password','email']