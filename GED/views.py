from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic.edit import FormView
from .models import Documento, Departamento, Pessoa,  Funcao, Anexo, Documento_Visibilidade
from .forms import DocumentoForms, DepartamentoForms, PessoaForms, FuncaoForms, AnexoForm, SharingForm

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
    documentos = Documento.objects.filter(pessoa_usuario=request.user) | Documento.objects.filter(pessoa_compartilha=request.user) | Documento.objects.filter(documento_privado=False).order_by('-data_cadastro')
    return render(request, 'dashboard.html', {'documentos':documentos})

@login_required
def dashboard_documentos(request):
    documentos = Documento.objects.filter(pessoa_usuario=request.user) | Documento.objects.filter(pessoa_compartilha=request.user) | Documento.objects.filter(documento_privado=False)
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
        anexo_form = AnexoForm(request.POST, request.FILES)
        sharing_form = SharingForm(request.POST)
        if documento_form.is_valid():
            documento_model = documento_form.save(commit=False)
            documento_model.pessoa_usuario = request.user
            documento_model.save()
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    anexo_form = Anexo(arquivo=formfile, documento = documento_model)
                    anexo_form.save()
            
            sharing_form = Documento_Visibilidade(documento = documento_model)
            sharing_form.save()

            return redirect('dashboard_documentos')
                
        else:
            context = {'documento_form':documento_form}
            return render(request, 'forms/document_form.html', context)
    else:
        sharing_form = SharingForm()
        documento_form = DocumentoForms()
        anexo_form = AnexoForm()
        context = {'documento_form':documento_form, 'anexo_form':anexo_form, 'sharing_form':sharing_form}
        return render(request, 'forms/document_form.html', context)

@login_required
def update_documento(request, id):
    documento = Documento.objects.get(id=id)
    anexos = Anexo.objects.select_related('documento').filter(documento__id=id)
    documento_form = DocumentoForms(instance=documento)
    anexo_form = AnexoForm(request.POST, request.FILES)
    sharing = Documento_Visibilidade.objects.all()
    sharing_form = SharingForm(request.POST)
    if request.method == 'POST':
        documento_form = DocumentoForms(request.POST, request.FILES, instance=documento)
        anexo_form = AnexoForm(request.POST, request.FILES)
        sharing_form = SharingForm(request.POST, instance=sharing)
        if documento_form.is_valid():
            documento_model = documento_form.save(commit=False)
            documento_model.save()
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    anexo_form = Anexo(arquivo=formfile, documento = documento_model)
                    anexo_form.save()           

            sharing_form = Documento_Visibilidade(documento = documento_model)
            sharing_form.save()
            return redirect('dashboard_documentos')

    return render(request, 'forms/document_form.html', {'documento_form': documento_form, 'documento': documento, 'anexo_form': anexo_form, 'anexos': anexos,'sharing_form':sharing_form, 'sharing':sharing})



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

@login_required
def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get (id=id)
    pessoa.delete()
    return redirect('dashboard_pessoas')


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

@login_required
def dashboard_funcao(request):
    funcao = Funcao.objects.all()
    return render(request, 'details_funcao.html', {'funcao': funcao})

@login_required
def create_funcao(request):
    if request.method == 'POST':
        funcao_form = FuncaoForms(request.POST)
        if funcao_form.is_valid():
            funcao_model = funcao_form.save(commit=False)
            funcao_model.save()
            return redirect('dashboard_funcao')
        else:
            context = {'funcao_form' : funcao_form}
            return render(request, 'forms/funcao_form.html', context)
    else:
        funcao_form = FuncaoForms()
        context = {'funcao_form':funcao_form}
        return render(request, 'forms/funcao_form.html', context)

@login_required
def update_funcao(request, id):
    funcao = Funcao.objects.get (id=id)
    funcao_form = FuncaoForms(request.POST or None,  instance=funcao)

    if funcao_form.is_valid():
        funcao_model = funcao_form.save(commit=False)
        funcao_model.save()
        return redirect('dashboard_funcao')
    else:
        context = {'funcao_form':funcao_form}
        return render(request, 'forms/funcao_form.html', context)
    
    return render(request, 'forms/funcao_form.html', {'funcao_form': funcao_form, 'funcao': funcao})

@login_required
def delete_funcao(request, id):
    funcao = Funcao.objects.get(id=id)
    funcao.delete()
    return redirect('dashboard_funcao')
