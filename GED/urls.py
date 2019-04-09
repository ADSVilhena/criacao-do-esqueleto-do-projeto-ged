from django.urls import path
from .views import list_documentos

urlpatterns = [
    path('', list_documentos, name = 'list_documento'),
]