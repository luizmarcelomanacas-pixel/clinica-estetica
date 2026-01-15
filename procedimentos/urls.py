from django.urls import path
from .views import (
    lista_procedimentos,
    novo_procedimento,
    editar_procedimento,
    excluir_procedimento
)

urlpatterns = [
    path('', lista_procedimentos, name='lista_procedimentos'),
    path('novo/', novo_procedimento, name='novo_procedimento'),
    path('editar/<int:procedimento_id>/', editar_procedimento, name='editar_procedimento'),
    path('excluir/<int:procedimento_id>/', excluir_procedimento, name='excluir_procedimento'),
]
