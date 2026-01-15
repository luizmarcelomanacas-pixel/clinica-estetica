from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'procedimento', 'data', 'hora', 'status')
    list_filter = ('status', 'data')
    search_fields = ('cliente__nome', 'procedimento__nome')
