from django.urls import path
from .views import update_departamento, delete_departamento, delete_pessoa, update_pessoa, delete_documento, update_documento, dashboard_pessoas, create_pessoa, create_departamentos, dashboard_departamentos, create_documents, list_documentos, buscar_documento, detalhes_documentos, dashboard, dashboard_documentos, dashboard_busca_documento, login_user, auth_user, logout_user

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
    path('dashboard/documentos/update/<int:id>/', update_documento, name='update_documento'),
    path('dashboard/documentos/delete/<int:id>/', delete_documento, name='delete_documento'),
    path('dashboard/departamentos/update/<int:id>/', update_departamento, name='update_departamento'),
    path('dashboard/departamentos/delete/<int:id>/', delete_departamento, name='delete_departamento'),
    path('dashboard/pessoas/update/<int:id>/', update_pessoa, name='update_pessoa'),
    path('dashboard/pessoas/delete/<int:id>/', delete_pessoa, name='delete_pessoa'),

    path('accounts/login/', login_user, name='login_user'),
    path('accounts/auth/', auth_user, name='auth_user'),
    path('accounts/logout/', logout_user, name='logout_user')
]