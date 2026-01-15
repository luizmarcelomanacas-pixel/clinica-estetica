from django.shortcuts import render
from .models import Pagamento

def lista_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    total_pago = sum(p.valor for p in pagamentos if p.status == 'pago')

    return render(request, 'financeiro/lista.html', {
        'pagamentos': pagamentos,
        'total_pago': total_pago
    })
from django.shortcuts import redirect, get_object_or_404
from agenda.models import Agendamento
from .models import Pagamento

def marcar_como_pago(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    # evita pagamento duplicado
    if not Pagamento.objects.filter(agendamento=agendamento).exists():
        Pagamento.objects.create(
            agendamento=agendamento,
            valor=agendamento.procedimento.preco,
            status='pago'
        )

    return redirect('lista_pagamentos')

from agenda.models import Agendamento
from .models import Pagamento

def agendamentos_pendentes(request):
    pagos = Pagamento.objects.values_list('agendamento_id', flat=True)
    agendamentos = Agendamento.objects.exclude(id__in=pagos)

    return render(request, 'financeiro/agendamentos.html', {
        'agendamentos': agendamentos
    })
from django.utils import timezone
from django.db.models import Sum
from datetime import date

def relatorio_diario(request):
    hoje = date.today()

    pagamentos = Pagamento.objects.filter(
        data_pagamento__date=hoje,
        status='pago'
    )

    total = pagamentos.aggregate(total=Sum('valor'))['total'] or 0

    return render(request, 'financeiro/relatorio_diario.html', {
        'pagamentos': pagamentos,
        'total': total,
        'data': hoje
    })


def relatorio_mensal(request):
    hoje = timezone.now()

    pagamentos = Pagamento.objects.filter(
        data_pagamento__year=hoje.year,
        data_pagamento__month=hoje.month,
        status='pago'
    )

    total = pagamentos.aggregate(total=Sum('valor'))['total'] or 0

    return render(request, 'financeiro/relatorio_mensal.html', {
        'pagamentos': pagamentos,
        'total': total,
        'mes': hoje.strftime('%m/%Y')
    })
from openpyxl import Workbook
from django.http import HttpResponse

def exportar_relatorio_diario_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório Diário"

    ws.append(["Cliente", "Procedimento", "Valor"])

    pagamentos = Pagamento.objects.filter(status='pago')

    for p in pagamentos:
        ws.append([
            p.agendamento.cliente.nome,
            p.agendamento.procedimento.nome,
            float(p.valor)
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=relatorio_diario.xlsx'
    wb.save(response)

    return response


def exportar_relatorio_mensal_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório Mensal"

    ws.append(["Cliente", "Procedimento", "Valor"])

    pagamentos = Pagamento.objects.filter(status='pago')

    for p in pagamentos:
        ws.append([
            p.agendamento.cliente.nome,
            p.agendamento.procedimento.nome,
            float(p.valor)
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=relatorio_mensal.xlsx'
    wb.save(response)

    return response
