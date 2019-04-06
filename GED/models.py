from django.contrib.auth.models import User
from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    ramal = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
class Funcao(models.Model):
    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True)

    def __str__(self):
        return self.nome

class Documento(models.Model):
    nome = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=1000)
    arquivo = models.FileField()
    pessoa_dono = models.ForeignKey(Pessoa, related_name='pessoa_doc_dono', verbose_name="Referente a", on_delete=models.PROTECT)
    pessoa_usuario = models.ForeignKey(User, related_name='pessoa_doc_usuario', verbose_name="Responsável", on_delete=models.PROTECT)
    documento_privado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Anexo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    documento = models.ForeignKey(Documento, on_delete=models.PROTECT)
    arquivo = models.FileField()
    def __str__(self):
        return self.nome

class Documento_Visibilidade(models.Model):
    class Meta:
        verbose_name = 'Visibilidade'
        verbose_name_plural = 'Visibilidades'
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    documento = models.ForeignKey(Documento, on_delete = models.PROTECT)
    visibilidade = models.BooleanField(default=True)

