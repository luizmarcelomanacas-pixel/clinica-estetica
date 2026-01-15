from django.urls import path
from .views import (
    lista_pagamentos,
    marcar_como_pago,
    agendamentos_pendentes,
    relatorio_diario,
    relatorio_mensal,
    exportar_relatorio_diario_excel,
    exportar_relatorio_mensal_excel,

)

urlpatterns = [
    path('', lista_pagamentos, name='lista_pagamentos'),
    path('pendentes/', agendamentos_pendentes, name='agendamentos_pendentes'),
    path('pagar/<int:agendamento_id>/', marcar_como_pago, name='marcar_como_pago'),
    path('relatorio/diario/', relatorio_diario, name='relatorio_diario'),
    path('relatorio/mensal/', relatorio_mensal, name='relatorio_mensal'),
    path('relatorio/diario/excel/', exportar_relatorio_diario_excel, name='exportar_relatorio_diario_excel'),
    path('relatorio/mensal/excel/', exportar_relatorio_mensal_excel, name='exportar_relatorio_mensal_excel'),

]
