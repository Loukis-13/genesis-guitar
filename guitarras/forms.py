from django import forms

from guitarras.models import Guitarra


class GuitarraForm(forms.ModelForm):
    class Meta:
        model = Guitarra
        fields = ['nome', 'cabeca', 'braco', 'corpo', 'capitador1', 'capitador2', 'preco']
