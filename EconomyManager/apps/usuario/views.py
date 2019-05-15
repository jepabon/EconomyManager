from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from EconomyManager.apps.usuario.models import Usuario
from EconomyManager.apps.usuario.form import UsuarioForm
from django.urls import reverse_lazy

class UsuarioIndexView(ListView):
    model = Usuario
class UsuarioCreacionView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario:index')

class UsuarioEdicionView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario:index')

class UsuarioEliminacionView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario:index')

class UsuarioDetalleView(DetailView):
    model = Usuario