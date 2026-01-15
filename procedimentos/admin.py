from django.contrib import admin
from .models import Procedimento

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
