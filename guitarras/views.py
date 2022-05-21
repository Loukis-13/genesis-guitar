from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from guitarras.forms import GuitarraForm

from .models import Guitarra


class GuitarraListaView(generic.ListView):
    def get_queryset(self):
        return Guitarra.objects.all()

def criar(request):
    return render(request, 'guitarras/criar.html')

class GuitarraView(generic.View):
    template_name = 'guitarras/criar.html'
    form_class = GuitarraForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        # guitarra = Guitarra(
        #     corpo=request.POST['corpo'],
        #     preco=request.POST['preco'],
        #     braco=request.POST['braco'],
        # )

        # guitarra.save()
        return redirect('/guitarras')

    def update(self, request, *args, **kwargs):
        return render(request, 'guitarras/criar.html')

    def delete(self, request, pk, *args, **kwargs):
        Guitarra.objects.get(id=pk).delete()
        return redirect('/guitarras')

def salvar(request):
    if request.method == 'POST':
        form = GuitarraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/guitarras')
    else:
        form = GuitarraForm()

    return render(request, 'guitarras/criar.html', {'form': form})

    guitarra = Guitarra(
        corpo=request.POST['corpo'],
        preco=request.POST['preco'],
        braco=request.POST['braco'],
    )

    guitarra.save()
    return redirect('/guitarras')

def editar(request, pk):
    return render(request, 'guitarras/criar.html')

def excluir(request, pk):
    Guitarra.objects.get(id=pk).delete()
    return redirect('/guitarras')
