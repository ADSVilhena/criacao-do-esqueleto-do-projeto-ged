from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Documento, Departamento, Pessoa
from .forms import DocumentoForms, DepartamentoForms, PessoaForms

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILE['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'dashboard_documentos', context)

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
    documentos = Documento.objects.filter()
    return render(request, 'dashboard.html', {'documentos':documentos})

def dashboard_documentos(request):
    documentos = Documento.objects.filter()
    return render(request, 'model-details.html', {'documentos':documentos})

def dashboard_busca_documento(request):
    campo_busca = request.POST['consulta']
    documentos = Documento.objects.filter(nome__contains = campo_busca)

    return render(request, 'model-details.html', {'documentos': documentos})

def create_documents(request):
    form = DocumentoForms(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('dashboard_documentos')
    return render(request, 'forms.html', {'form':form})

def dashboard_departamentos(request):
    departamento = Departamento.objects.all()
    return render(request, 'details_departamento.html', {'departamento': departamento})

def create_departamentos(request):
    form = DepartamentoForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard_departamentos')
    return render(request, 'forms.html', {'form': form})

def dashboard_pessoas(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'details_people.html', {'pessoa': pessoa})

def create_pessoa(request):
    form = PessoaForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('dashboard_pessoas')
    return render(request, 'forms.html', {'form': form})


def update_documento(request, id):
    documento = Documento.objects.get (id=id)
    form = DocumentoForms(request.POST,  request.FILES,  instance=documento)
    if form.is_valid():
        form.save()
        return redirect('dashboard_documentos')
    return render(request, 'forms.html', {'form': form, 'documento': documento})


def delete_documento(request, id):
    documento = Documento.objects.get(id=id)
    if request.method == 'POST':
        documento.delete()
        return redirect('dashboard_documentos')
    return render(request, 'message.html', {'documento': documento})    

def update_documento(request, id):
    documento = Documento.objects.get (id=id)
    form = DocumentoForms(request.POST or None,  instance=documento)
    if form.is_valid():
        form.save()
        return redirect('dashboard_documentos')
    return render(request, 'forms.html', {'form': form, 'documento': documento})

def delete_documento(request, id):
    documento = Documento.objects.get(id=id)
    if request.method == 'POST':
        documento.delete()
        return redirect('dashboard_documentos')
    return render(request, 'message.html', {'documento': documento})    

def update_pessoa(request, id):
    pessoa = Pessoa.objects.get (id=id)
    form = PessoaForms(request.POST or None,  instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('dashboard_pessoas')
    return render(request, 'forms.html', {'form': form, 'pessoa': pessoa})


def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get (id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('dashboard_pessoas')
    return render(request, 'message.html', {'pessoa': pessoa})    


def update_departamento(request, id):
    departamento = Departamento.objects.get (id=id)
    form = DepartamentoForms(request.POST or None,  instance=departamento)
    if form.is_valid():
        form.save()
        return redirect('dashboard_departamentos')
    return render(request, 'forms.html', {'form': form, 'departamento': departamento})


def delete_departamento(request, id):
    departamento = Departamento.objects.get (id=id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('dashboard_departamentos')
    return render(request, 'message.html', {'departamento': departamento})    