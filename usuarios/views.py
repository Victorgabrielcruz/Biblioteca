from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256

# Create your views here.
def login(request):
    return HttpResponse('Login')

def cadastro(request):
    status = request.GET.get('status')
    return render(request,'cadastro.html')

from django.shortcuts import redirect
from django.http import HttpResponse

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if not nome.strip() or not email.strip():
        return redirect('/auth/cadastro/?status=1')
    elif len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')
    try:
        usuario_existe = Usuario.objects.filter(email=email).exists()
    except Exception as e:
        return HttpResponse(f"Erro ao verificar usuário: {e}")

    if usuario_existe:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except Exception as e:
        return redirect('/auth/cadastro/?status=4')
