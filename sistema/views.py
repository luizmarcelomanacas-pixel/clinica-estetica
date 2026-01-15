from django.shortcuts import render
from clientes.models import Cliente
from agenda.models import Agendamento
from datetime import date

def dashboard(request):
    total_clientes = Cliente.objects.count()
    agendamentos_hoje = Agendamento.objects.filter(data=date.today()).count()

    return render(request, 'dashboard.html', {
        'total_clientes': total_clientes,
        'agendamentos_hoje': agendamentos_hoje
    })
