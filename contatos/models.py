from django.db import models
from django.utils import timezone
# Create your models here.


class Categoria (models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contatos (models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=255, blank=True)
    datacriacao = models.DateTimeField(default=timezone.now)
    descricao = models.CharField(max_length=255, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome
