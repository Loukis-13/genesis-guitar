from django.shortcuts import render

from .models import Guitarra

def index(request):
    return render(request, 'guitarras/inicio.html')

def editar(request):
    return render(request, 'guitarras/criar.html')

def salvar(request):
    print(request.POST)
    guitarra = Guitarra(corpo=request.POST['corpo'])
    print(guitarra)
    return render(request, 'guitarras/inicio.html')