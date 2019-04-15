from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Documento

def list_documentos(request):
    obj = Documento.objects.all()
    for abc in obj:
        obj_nome = abc.nome
        obj_descricao = abc.descricao
        obj_pessoa_dono = abc.pessoa_dono
        obj_pessoa_usuario = abc.pessoa_usuario

    context = {
        "obj":obj,
        "obj_nome":obj_nome,
        "obj_descricao":obj_descricao,
        "obj_pessoa_dono":obj_pessoa_dono,
        "obj_pessoa_usuario":obj_pessoa_usuario
    }
    return render(request, 'documentos.html', context)

def buscar_documento(request):
    campo_busca = request.POST['consulta']
    obj = Documento.objects.filter(nome__contains = campo_busca)
    for abc in obj:
        obj_nome = abc.nome
        obj_descricao = abc.descricao
        obj_pessoa_dono = abc.pessoa_dono
        obj_pessoa_usuario = abc.pessoa_usuario

    context = {
        "obj":obj,
        "obj_nome":obj_nome,
        "obj_descricao":obj_descricao,
        "obj_pessoa_dono":obj_pessoa_dono,
        "obj_pessoa_usuario":obj_pessoa_usuario
    }
    return render(request, 'buscar.html', context)