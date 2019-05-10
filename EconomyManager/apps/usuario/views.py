from django.views.generic import CreateView, UpdateView, ListView
from EconomyManager.apps.usuario.models import Usuario
from EconomyManager.apps.usuario.form import UsuarioForm
from django.urls import reverse_lazy

class UsuarioIndexView(ListView):
    model = Usuario
class UsuarioCreacionView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('app_base:index')

class UsuarioEdicionView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('app_base:index')