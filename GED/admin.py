from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Departamento, Funcao, Pessoa, Documento, Anexo, Documento_Visibilidade

class DepartamentoAdmin(admin.ModelAdmin):
    model = Departamento
    list_display = ['nome', 'ramal']

class DocumentoAdmin(admin.ModelAdmin):
    model: Documento
    list_display = ['nome', 'descricao', 'arquivo', 'pessoa_dono', 'documento_privado']
    search_fields = ('nome', 'descricao')

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcao)
admin.site.register(Pessoa)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Anexo)
admin.site.register(Documento_Visibilidade)