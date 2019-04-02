from django.contrib.auth.models import User
from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    ramal = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
class Funcao(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT)

