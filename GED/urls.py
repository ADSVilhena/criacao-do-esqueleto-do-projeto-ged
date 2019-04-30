from django.urls import path
from .views import dashboard_pessoas, create_pessoa, create_departamentos, dashboard_departamentos, create_documents, list_documentos, buscar_documento, detalhes_documentos, dashboard, dashboard_documentos, dashboard_busca_documento

urlpatterns = [
    path('', list_documentos, name = 'list_documento'),
    path('buscar/', buscar_documento, name = 'buscar_documento'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('detalhes/<int:id>/', detalhes_documentos, name='detalhes_documentos'),
    path('dashboard/documentos/', dashboard_documentos, name='dashboard_documentos'),
    path('dashboard/documentos/buscar', dashboard_busca_documento, name='dashboard_busca_documentos'),
    path('dashboard/documentos/novo', create_documents, name='create_documents'),
    path('dashboard/departamentos', dashboard_departamentos, name='dashboard_departamentos'),
    path('dashboard/departamentos/novo', create_departamentos, name='create_departamentos'),
    path('dashboard/pessoas', dashboard_pessoas, name='dashboard_pessoas'),
    path('dashboard/pessoa/novo', create_pessoa, name='create_pessoa'),

]