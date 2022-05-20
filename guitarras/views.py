from django.shortcuts import redirect, render

from .models import Guitarra

def index(request):
    return render(request, 'guitarras/lista.html', {'guitarras': Guitarra.objects.all()})

def editar(request):
    return render(request, 'guitarras/criar.html')

def salvar(request):
    print(request.POST)
    guitarra = Guitarra(
        corpo=request.POST['corpo'],
        preco=request.POST['preco'],
    )
    print(guitarra)

    guitarra.save()
    return redirect('/guitarras')
