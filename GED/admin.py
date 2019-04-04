from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Departamento, Funcao, Pessoa



class DepartamentoAdmin(admin.ModelAdmin):
    model = Departamento
    list_display = ['nome', 'ramal']

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcao)
admin.site.register(Pessoa)