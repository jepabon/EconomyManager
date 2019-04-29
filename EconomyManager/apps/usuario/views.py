from django.shortcuts import render
from django.views.generic import TemplateView
from django.http.response import HttpResponse

class LoginView(TemplateView):
    def get(self,request, *args, **kwargs):
        return HttpResponse('hola mundo')
