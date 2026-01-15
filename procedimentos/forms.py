from django import forms
from .models import Procedimento

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = ['nome', 'preco']
