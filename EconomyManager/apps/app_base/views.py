from django.shortcuts import render,redirect
from django.views.generic import View, UpdateView, DetailView, ListView, DeleteView, CreateView
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate,login,logout

class LoginView(View):
    def get(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('app_base:index')
        return render(request,'app_base/login.html',{})
    def post(self,request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario and usuario.is_active:
            login(request,usuario)
            return redirect('app_base:index')
        return redirect('app_base:login')

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('app_base:login')

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'app_base/index.html',{})

