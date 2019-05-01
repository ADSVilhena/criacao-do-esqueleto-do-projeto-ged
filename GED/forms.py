from django import forms
from . import models

pessoa_dono = forms.ModelChoiceField(queryset=models.Documento.objects.all(), required=False)
pessoa_usuario = forms.ModelChoiceField(queryset=models.Documento.objects.all(),required=False)
   
class DocumentoForms(forms.ModelForm):
    class Meta:
        model = models.Documento
        fields = ['nome', 'descricao', 'pessoa_dono', 'pessoa_usuario', 'documento_privado', 'arquivo']
        required = False

class DepartamentoForms(forms.ModelForm):
    class Meta:
        model = models.Departamento
        fields = ['nome', 'ramal']

class PessoaForms(forms.ModelForm):
    class Meta:
        model = models.Pessoa
        fields = ['nome', 'endereco', 'telefone', 'email', 'departamento', 'funcao', 'user']
        required = False

