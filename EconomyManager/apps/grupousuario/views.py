from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.auth.models import Group
from EconomyManager.apps.usuario.models import Usuario
from EconomyManager.apps.grupousuario.form import GrupoUsuarioForm
from django.urls import reverse_lazy

class GrupoUsuarioIndexView(ListView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = Usuario.objects.all()
        return context
    
class GrupoUsuarioCreacionView(CreateView):
    model = Group
    form_class = GrupoUsuarioForm
    success_url = reverse_lazy('grupousuario:index')

class GrupoUsuarioEdicionView(UpdateView):
    model = Group
    form_class = GrupoUsuarioForm
    success_url = reverse_lazy('grupousuario:index')

class GrupoUsuarioEliminacionView(DeleteView):
    model = Group
    success_url = reverse_lazy('grupousuario:index')

class GrupoUsuarioDetalleView(DetailView):
    model = Group