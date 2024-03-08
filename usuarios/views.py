from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
# Create your views here.
def login(request):
    return HttpResponse('Login')

def cadastro(request):
    return render(request,'cadastro.html')

def valida_cadastro(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario(nome = nome, email = email, senha = senha)
    return HttpResponse(f"{nome, email, senha}")
    usuario.save()