from django.db import models
from agenda.models import Agendamento

class Pagamento(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
    )

    agendamento = models.OneToOneField(
        Agendamento,
        on_delete=models.CASCADE
    )
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pago'
    )
    data_pagamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.agendamento} - {self.status}'
