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
    if request.method == 'POST':
        documento_form = DocumentoForms(request.POST, request.FILES)
        if documento_form.is_valid():
            documento_model = documento_form.save(commit=False)
            documento_model.save()
            return redirect('dashboard_documentos')
        else:
            context = {'documento_form':documento_form}
            return render(request, 'forms/document_form.html', context)
    else:
        documento_form = DocumentoForms()
        context = {'documento_form':documento_form}
        return render(request, 'forms/document_form.html', context)

@login_required
def update_documento(request, id):
    # documento = Documento.objects.get (id=id)
    # documento_form = DocumentoForms(request.POST,  instance=documento)
    # if documento_form.is_valid():
    #     documento_model = documento_form.save(commit=False)
    #     documento_model.save()
    #     return redirect('dashboard_documentos')
    # else:
    #     context = {'documento_form':documento_form}
    #     return render(request, 'forms/document_form.html', context)

    documento = Documento.objects.get (id=id)
    documento_form = DocumentoForms(instance=documento)
    if request.method == 'POST':
        documento_form = DocumentoForms(request.POST, request.FILES, instance=documento)
        if documento_form.is_valid():
            documento_form.save()
            return redirect('dashboard_documentos')
    return render(request, 'forms/document_form.html', {'documento_form': documento_form, 'documento': documento})


# def create_documents(request):
#     form = DocumentoForms(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('dashboard_documentos')
#     return render(request, 'forms/document_form.html', {'form':form})

@login_required
def dashboard_departamentos(request):
    departamento = Departamento.objects.all()
    return render(request, 'details_departamento.html', {'departamento': departamento})

def create_departamentos(request):
    if request.method == 'POST':
        departamento_form = DepartamentoForms(request.POST)
        if departamento_form.is_valid():
            departamento_model = departamento_form.save(commit=False)
            departamento_model.save()
            return redirect('dashboard_departamentos')
        else:
            context = {'departamento_form':departamento_form}
            return render(request, 'forms/departamento_form.html', context)
    else:
        departamento_form = DepartamentoForms()
        context = {'departamento_form':departamento_form}
        return render(request, 'forms/departamento_form.html', context)

# @login_required
# def create_departamentos(request):
#     form = DepartamentoForms(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('dashboard_departamentos')
#     return render(request, 'forms.html', {'form': form})

@login_required
def dashboard_pessoas(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'details_people.html', {'pessoa': pessoa})

@login_required
def create_pessoa(request):
    if request.method == 'POST':
        pessoa_form = PessoaForms(request.POST)
        if pessoa_form.is_valid():
            pessoa_model = pessoa_form.save(commit=False)
            pessoa_model.save()
            return redirect('dashboard_pessoas')
        else:
            context = {'pessoa_form' : pessoa_form}
            return render(request, 'forms/pessoa_form.html', context)
    else:
        pessoa_form = PessoaForms()
        context = {'pessoa_form':pessoa_form}
        return render(request, 'forms/pessoa_form.html', context)

@login_required
def update_pessoa(request, id):
    pessoa = Pessoa.objects.get (id=id)
    pessoa_form = PessoaForms(request.POST or None,  instance=pessoa)

    if pessoa_form.is_valid():
        pessoa_model = pessoa_form.save(commit=False)
        pessoa_model.save()
        return redirect('dashboard_pessoas')
    else:
        context = {'pessoa_form':pessoa_form}
        return render(request, 'forms/pessoa_form.html', context)
    
    return render(request, 'forms/pessoa_form.html', {'pessoa_form': pessoa_form, 'pessoa': pessoa})


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
def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get (id=id)
    pessoa.delete()
    return redirect('dashboard_pessoas')

#  if request.method == 'POST':
#         departamento_form = DepartamentoForms(request.POST)
#         if departamento_form.is_valid():
#             departamento_model = departamento_form.save(commit=False)
#             departamento_model.save()
#             return redirect('dashboard_departamentos')
#         else:
#             context = {'departamento_form':departamento_form}
#             return render(request, 'forms/departamento_form.html', context)
#     else:
#         departamento_form = DepartamentoForms()
#         context = {'departamento_form':departamento_form}
#         return render(request, 'forms/departamento_form.html', context)

@login_required
def update_departamento(request, id):
    departamento = Departamento.objects.get (id=id)
    departamento_form = DepartamentoForms(request.POST or None,  instance=departamento)
    if departamento_form.is_valid():
        departamento_model = departamento_form.save(commit=False)
        departamento_model.save()
        return redirect('dashboard_departamentos')
    else:
        context = {'departamento_form':departamento_form}
        return render(request, 'forms/departamento_form.html', context)

    return render(request, 'forms/departamento_form.html', {'departamento_form': departamento_form, 'departamento': departamento})

@login_required
def delete_departamento(request, id):
    departamento = Departamento.objects.get (id=id)
    departamento.delete()
    return redirect('dashboard_departamentos')