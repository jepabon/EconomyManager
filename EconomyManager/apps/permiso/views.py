from django.shortcuts import render
from django.contrib.auth.models import Permission
from django.views.generic import ListView

class PermisoIndexView(ListView):
    model = Permission