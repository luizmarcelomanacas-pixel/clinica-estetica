from django.shortcuts import render
from django.http import JsonResponse

from .models import Agendamento
from clientes.models import Cliente
from procedimentos.models import Procedimento

def agenda_calendario(request):
    agendamentos = Agendamento.objects.all()

    eventos = []
    for ag in agendamentos:
        eventos.append({
            'id': ag.id,
            'title': f'{ag.cliente.nome} - {ag.procedimento.nome}',
            'start': f'{ag.data}T{ag.hora}',
        })

    return render(request, 'agenda/calendario.html', {
        'eventos': eventos,
        'clientes': Cliente.objects.all(),
        'procedimentos': Procedimento.objects.all(),
    })

from django.http import JsonResponse
from clientes.models import Cliente
from procedimentos.models import Procedimento
from .models import Agendamento

def criar_agendamento(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        procedimento_id = request.POST.get('procedimento')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        agendamento = Agendamento.objects.create(
            cliente=Cliente.objects.get(id=cliente_id),
            procedimento=Procedimento.objects.get(id=procedimento_id),
            data=data,
            hora=hora
        )

        return JsonResponse({
            'id': agendamento.id,
            'title': f'{agendamento.cliente.nome} - {agendamento.procedimento.nome}',
            'start': f'{agendamento.data}T{agendamento.hora}'
        })
def editar_agendamento(request):
    if request.method == 'POST':
        ag = Agendamento.objects.get(id=request.POST.get('id'))
        ag.hora = request.POST.get('hora')
        ag.save()
        return JsonResponse({'ok': True})

def excluir_agendamento(request):
    if request.method == 'POST':
        Agendamento.objects.get(id=request.POST.get('id')).delete()
        return JsonResponse({'ok': True})
