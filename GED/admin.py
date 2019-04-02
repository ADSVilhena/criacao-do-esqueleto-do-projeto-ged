from django.contrib import admin

from .models import Departamento, Funcao, Pessoa

admin.site.register(Departamento)
admin.site.register(Funcao)
admin.site.register(Pessoa)