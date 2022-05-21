from django.db import models


class Guitarra(models.Model):
    nome = models.CharField("Nome da guitarra", max_length=20)
    cabeca = models.CharField("Cabeça", max_length=20, blank=False, null=False, choices=(
        ('jackson', 'Jackson'),
        ('flying-v_1980', 'Flying-V 1980'),
        ('les_paul', 'Les Paul'),
        ('warlock', 'Warlock'),
    ))
    braco = models.CharField("Braço", max_length=20, choices=(
        ('circulos', 'Circulos'),
        ('triangulos', 'Triangulos'),
        ('retangulos', 'Retangulos'),
    ))
    corpo = models.CharField("Corpo", max_length=20, choices=(
        ('flying-v', 'Flying-V'),
        ('explorer', 'Explorer'),
        ('les_paul', 'Les Paul'),
        ('warlock', 'Warlock'),
        ('sg', 'SG'),
    ))
    capitador1 = models.CharField("Capitador ponte", max_length=20, choices=(
        ('humbucker1', 'Humbucker'),
        ('singlecoil1', 'Singlecoil'),
    ))
    capitador2 = models.CharField("Capitador braço", max_length=20, choices=(
        ('humbucker2', 'Humbucker'),
        ('singlecoil2', 'Singlecoil'),
    ))
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=8)
    imagem = models.CharField(max_length=20)
    criacao = models.DateTimeField('data de criação', auto_now=True)
