from django.views import generic

from .models import Guitarra


class GuitarraListaView(generic.ListView):
    def get_queryset(self):
        return Guitarra.objects.all()

class CriarGuitarraView(generic.CreateView):
    model = Guitarra
    fields = ('nome', 'cabeca', 'braco', 'corpo', 'capitador1', 'capitador2', 'preco')

class EditarGuitarraView(generic.UpdateView):
    model = Guitarra
    fields = ('nome', 'cabeca', 'braco', 'corpo', 'capitador1', 'capitador2', 'preco')

class ExcluirGuitarraView(generic.DeleteView):
    model = Guitarra
