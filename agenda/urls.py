from django.urls import path
from .views import (
    agenda_calendario,
    criar_agendamento,
    editar_agendamento,
    excluir_agendamento
)

urlpatterns = [
    path('', agenda_calendario, name='agenda'),
    path('criar/', criar_agendamento, name='criar_agendamento'),
    path('editar/', editar_agendamento, name='editar_agendamento'),
    path('excluir/', excluir_agendamento, name='excluir_agendamento'),
]
