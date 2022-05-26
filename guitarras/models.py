from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Guitarra(models.Model):
    nome = models.CharField("Nome da guitarra", max_length=20)
    cabeca = models.CharField("Cabeça", max_length=20, blank=False, null=False, default="", choices=(
        ('jackson', 'Jackson'),
        ('flying-v_1980', 'Flying-V 1980'),
        ('les_paul', 'Les Paul'),
        ('warlock', 'Warlock'),
    ))
    braco = models.CharField("Braço", max_length=20, blank=False, null=False, default="",  choices=(
        ('circulos', 'Circulos'),
        ('triangulos', 'Triangulos'),
        ('retangulos', 'Retangulos'),
    ))
    corpo = models.CharField("Corpo", max_length=20, blank=False, null=False, default="",  choices=(
        ('flying-v', 'Flying-V'),
        ('explorer', 'Explorer'),
        ('les_paul', 'Les Paul'),
        ('warlock', 'Warlock'),
        ('sg', 'SG'),
    ))
    capitador1 = models.CharField("Capitador ponte", max_length=20, blank=False, null=False, default="",  choices=(
        ('humbucker1', 'Humbucker'),
        ('singlecoil1', 'Singlecoil'),
        ('vazio', 'Sem capitador'),
    ))
    capitador2 = models.CharField("Capitador braço", max_length=20, null=False, default="",  choices=(
        ('humbucker2', 'Humbucker'),
        ('singlecoil2', 'Singlecoil'),
        ('vazio', 'Sem capitador'),
    ))
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=7, validators=[MinValueValidator(0)])
    imagem = models.CharField(max_length=20)
    criacao = models.DateTimeField('data de criação', auto_now=True)

    def get_absolute_url(self):
        return reverse("guitarras:guitarras")
        