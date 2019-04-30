from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Documento


def list_documentos(request):
    documentos = Documento.objects.filter(documento_privado=False)
    return render(request, 'documentos.html', {'documentos': documentos})

def buscar_documento(request):
    campo_busca = request.POST['consulta']
    documentos = Documento.objects.filter(nome__contains = campo_busca).filter(documento_privado=False)

    return render(request, 'documentos.html', {'documentos': documentos})

def detalhes_documentos(request, id):
    documento = Documento.objects.get   (pk=id)
    return render(request, 'detalhes.html', {'documento': documento})
    
def dashboard(request):
    documentos = Documento.objects.filter(documento_privado=False)
    return render(request, 'dashboard.html', {'documentos':documentos})
