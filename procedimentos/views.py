from django.shortcuts import render, redirect, get_object_or_404
from .models import Procedimento
from .forms import ProcedimentoForm

def lista_procedimentos(request):
    procedimentos = Procedimento.objects.all()
    return render(request, 'procedimentos/lista.html', {
        'procedimentos': procedimentos
    })

def novo_procedimento(request):
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_procedimentos')
    else:
        form = ProcedimentoForm()

    return render(request, 'procedimentos/novo.html', {'form': form})

def editar_procedimento(request, procedimento_id):
    procedimento = get_object_or_404(Procedimento, id=procedimento_id)

    if request.method == 'POST':
        form = ProcedimentoForm(request.POST, instance=procedimento)
        if form.is_valid():
            form.save()
            return redirect('lista_procedimentos')
    else:
        form = ProcedimentoForm(instance=procedimento)

    return render(request, 'procedimentos/editar.html', {
        'form': form,
        'procedimento': procedimento
    })

def excluir_procedimento(request, procedimento_id):
    procedimento = get_object_or_404(Procedimento, id=procedimento_id)

    if request.method == 'POST':
        procedimento.delete()
        return redirect('lista_procedimentos')

    return render(request, 'procedimentos/excluir.html', {
        'procedimento': procedimento
    })
from django.shortcuts import render

# Create your views here.
