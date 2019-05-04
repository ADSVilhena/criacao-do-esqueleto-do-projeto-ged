from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Documento, Departamento, Pessoa
from .forms import DocumentoForms, DepartamentoForms, PessoaForms

def login_user(request):
    next = request.GET.get('next', '/dashboard') 
    return render(request, 'login.html', {'next': next})

def auth_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    next = request.POST['next']

    if user is not None:
        login(request, user)
        if next:
            return redirect(next)
        else:
            return redirect('dashboard')
    else:
        return render(request, 'login.html', {'error': 'Usuário ou senha estão inválidos'})

@login_required
def logout_user(request):
    logout(request)
    return redirect('list_documento')

@login_required
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

@login_required
def dashboard(request):
    documentos = Documento.objects.filter()
    return render(request, 'dashboard.html', {'documentos':documentos})

@login_required
def dashboard_documentos(request):
    documentos = Documento.objects.filter()
    return render(request, 'details_documentos.html', {'documentos':documentos})

@login_required
def dashboard_busca_documento(request):
    campo_busca = request.POST['consulta']
    documentos = Documento.objects.filter(nome__contains = campo_busca)

    return render(request, 'details_documentos.html', {'documentos': documentos})

@login_required
def create_documents(request):
    form = DocumentoForms(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('dashboard_documentos')
    return render(request, 'forms.html', {'form':form})

@login_required
def dashboard_departamentos(request):
    departamento = Departamento.objects.all()
    return render(request, 'details_departamento.html', {'departamento': departamento})

@login_required
def create_departamentos(request):
    form = DepartamentoForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard_departamentos')
    return render(request, 'forms.html', {'form': form})

@login_required
def dashboard_pessoas(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'details_people.html', {'pessoa': pessoa})

@login_required
def create_pessoa(request):
    form = PessoaForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('dashboard_pessoas')
    return render(request, 'forms.html', {'form': form})

@login_required
def update_documento(request, id):
    documento = Documento.objects.get (id=id)
    form = DocumentoForms(request.POST,  request.FILES,  instance=documento)
    if form.is_valid():
        form.save()
        return redirect('dashboard_documentos')
    return render(request, 'forms.html', {'form': form, 'documento': documento})

@login_required
def delete_documento(request, id):
    documento = Documento.objects.get(id=id)
    documento.delete()
    return redirect('dashboard_documentos')

#@login_required    
#def update_documento(request, id):
#    documento = Documento.objects.get (id=id)
#    form = DocumentoForms(request.POST or None,  instance=documento)
#    if form.is_valid():
#        form.save()
#        return redirect('dashboard_documentos')
#    return render(request, 'forms.html', {'form': form, 'documento': documento})

#@login_required
#def delete_documento(request, id):
#    documento = Documento.objects.get(id=id)
#    if request.method == 'POST':
#        documento.delete()
#        return redirect('dashboard_documentos')
#    return render(request, 'message.html', {'documento': documento})    

@login_required
def update_pessoa(request, id):
    pessoa = Pessoa.objects.get (id=id)
    form = PessoaForms(request.POST or None,  instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('dashboard_pessoas')
    return render(request, 'forms.html', {'form': form, 'pessoa': pessoa})

@login_required
def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get (id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('dashboard_pessoas')
    return render(request, 'message.html', {'pessoa': pessoa})    

@login_required
def update_departamento(request, id):
    departamento = Departamento.objects.get (id=id)
    form = DepartamentoForms(request.POST or None,  instance=departamento)
    if form.is_valid():
        form.save()
        return redirect('dashboard_departamentos')
    return render(request, 'forms.html', {'form': form, 'departamento': departamento})

@login_required
def delete_departamento(request, id):
    departamento = Departamento.objects.get (id=id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('dashboard_departamentos')
    return render(request, 'message.html', {'departamento': departamento})    