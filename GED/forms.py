from django.forms import ModelForm, DateInput
from django import forms

from . import models
from django.forms.widgets import FileInput
from django.contrib.admin.widgets import AdminDateWidget


class DocumentoForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            self.fields['pessoa_dono'].required = False
            self.fields['pessoa_compartilha'].required = False
            self.fields['pessoa_usuario'].required = False


            if not isinstance(field.widget, FileInput):
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control-file'})
                field.widget.attrs.update({'multiple': True})
    class Meta:
        model = models.Documento
        fields = '__all__'
    
class AnexoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control-file'})
            field.widget.attrs.update({'multiple': True})

    class Meta:
        model = models.Anexo
        fields = '__all__'
            
class SharingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = models.Documento_Visibilidade
        fields = '__all__'
            

class DepartamentoForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            self.fields['ramal'].required = False

    class Meta:
        model = models.Departamento
        fields = '__all__'

class PessoaForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            self.fields['endereco'].required = False
            self.fields['email'].required = False
            self.fields['funcao'].required = False
            self.fields['user'].required = False
            self.fields['departamento'].required = False
            self.fields['telefone'].required = False
    class Meta:
        model = models.Pessoa
        fields = '__all__'

class FuncaoForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
         
    class Meta:
        model = models.Funcao
        fields = '__all__'