from django.db import models

class Guitarra(models.Model):
    nome = models.CharField(max_length=20)
    cabeca = models.CharField(max_length=20)
    braco = models.CharField(max_length=20)
    corpo = models.CharField(max_length=20)
    capitador1 = models.CharField(max_length=20)
    capitador2 = models.CharField(max_length=20)
    imagem = models.CharField(max_length=20)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    criacao = models.DateTimeField('data de criação', auto_now=True)

    def __str__(self) -> str:
        return f"{self.nome} {self.corpo}"
        