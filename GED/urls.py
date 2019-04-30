from django.urls import path
from .views import list_documentos, buscar_documento, detalhes_documentos, dashboard

urlpatterns = [
    path('', list_documentos, name = 'list_documento'),
    path('buscar/', buscar_documento, name = 'buscar_documento'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('detalhes/<int:id>/', detalhes_documentos, name='detalhes_documentos')
]