from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def Login(request,template_name='login.html'):
    next=request.GET.get('next','/dashboard/')
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            messages.error(request,'Usuário ou senha incorretos')
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request,template_name,{'redirect_to':next})

@login_required
def dashboard(request,template_name='dashboard.html'):

    return render(request,template_name,{})

@login_required
def resistrarUsuario(request, template_name='userNew.html'):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        tipo=request.POST['tipo-user']
        if tipo=='Administrador':
            user=User.objects.create_user(username,email,password)
            user.is_staff=True
            user.save()
        else:
            user=User.objects.create_user(username,email,password)
            messages.error(request,'Permissão de registro negada!')
        return redirect('/login/')
    return render(request,template_name,{})

def deslogar(request):
   logout(request)
   return HttpResponseRedirect(settings.LOGIN_URL)

class ColaboraForm(ModelForm):
    class Meta:
        model=Colaborador
        fields=['nome','nascimento','rg','cpf','sexo_choices']

@login_required
def ColaboradorNew(request, template_name='colaboradorNew.html'):
    form=ColaboraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    return render(request,template_name,{'form':form})

@login_required
def ListarUsuario(request,template_name='listuser.html'):
    usuario=User.objects.all()

    usuarios={'usuario':usuario}
    return render(request,template_name,usuarios)