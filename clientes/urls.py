from django.urls import path
from .views import (
    lista_clientes,
    novo_cliente,
    editar_cliente,
    excluir_cliente
)

urlpatterns = [
    path('', lista_clientes, name='lista_clientes'),
    path('novo/', novo_cliente, name='novo_cliente'),
    path('editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('excluir/<int:cliente_id>/', excluir_cliente, name='excluir_cliente'),
]
