from django.forms import ModelForm, DateInput
from django import forms

from . import models
from django.forms.widgets import FileInput
from django.contrib.auth.models import User
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
            self.fields['email'].widget = forms.HiddenInput()
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

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            self.fields['password'].label = "Senha"
            self.fields['last_login'].widget = forms.HiddenInput()
            self.fields['is_superuser'].widget = forms.HiddenInput()
            self.fields['user_permissions'].widget = forms.HiddenInput()
            self.fields['is_staff'].widget = forms.HiddenInput()
            self.fields['date_joined'].widget = forms.HiddenInput()
            self.fields['is_active'].widget = forms.HiddenInput()
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = '__all__'