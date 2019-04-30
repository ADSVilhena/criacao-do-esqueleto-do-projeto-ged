from django import forms
from . import models


class DocumentoForms(forms.ModelForm):
    class Meta:
        model = models.Documento
        fields = ['nome', 'descricao', 'arquivo', 'pessoa_dono', 'pessoa_usuario', 'documento_privado']

class DepartamentoForms(forms.ModelForm):
    class Meta:
        model = models.Departamento
        fields = ['nome', 'ramal']

class PessoaForms(forms.ModelForm):
    class Meta:
        model = models.Pessoa
        fields = ['nome', 'endereco', 'telefone', 'email', 'departamento', 'funcao', 'user']