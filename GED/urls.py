from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_documentos, name = 'list_documento'),
    path('buscar/', views.buscar_documento, name = 'buscar_documento'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('detalhes/<int:id>/', views.detalhes_documentos, name='detalhes_documentos')
    ,
    path('dashboard/documentos/', views.dashboard_documentos, name='dashboard_documentos'),
    path('dashboard/documentos/buscar', views.dashboard_busca_documento, name='dashboard_busca_documentos'),
    path('dashboard/documentos/novo', views.create_documents, name='create_documents'),
    path('dashboard/documentos/update/<int:id>/', views.update_documento, name='update_documento'),
    path('dashboard/documentos/delete/<int:id>/', views.delete_documento, name='delete_documento'),

    path('dashboard/departamentos', views.dashboard_departamentos, name='dashboard_departamentos'),
    path('dashboard/departamentos/novo', views.create_departamentos, name='create_departamentos'),
    path('dashboard/departamentos/update/<int:id>/', views.update_departamento, name='update_departamento'),
    path('dashboard/departamentos/delete/<int:id>/', views.delete_departamento, name='delete_departamento'),

    path('dashboard/pessoas', views.dashboard_pessoas, name='dashboard_pessoas'),
    path('dashboard/pessoa/novo', views.create_pessoa, name='create_pessoa'),
    path('dashboard/pessoas/update/<int:id>/', views.update_pessoa, name='update_pessoa'),
    path('dashboard/pessoas/delete/<int:id>/', views.delete_pessoa, name='delete_pessoa'),

    path('dashboard/funcao', views.dashboard_funcao, name='dashboard_funcao'),
    path('dashboard/funcao/novo', views.create_funcao, name='create_funcao'),
    path('dashboard/funcao/update/<int:id>/', views.update_funcao, name='update_funcao'),
    path('dashboard/funcao/delete/<int:id>/', views.delete_funcao, name='delete_funcao'),

    path('accounts/login/', views.login_user, name='login_user'),
    path('accounts/auth/', views.auth_user, name='auth_user'),
    path('accounts/logout/', views.logout_user, name='logout_user'),

    path('users/', views.create_user, name='users'),
    path('users/create/', views.create_user, name='create_user'),
]