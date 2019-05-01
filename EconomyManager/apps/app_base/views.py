from django.shortcuts import render
from django.views.generic import View, UpdateView, DetailView, ListView, DeleteView, CreateView
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

class LoginView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'app_base/login.html',{})
    def post(self,request, *args, **kwargs):
        print(request.POST)
        return HttpResponse('funciona hp')