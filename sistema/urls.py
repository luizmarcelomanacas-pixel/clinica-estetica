from django.contrib import admin
from django.urls import path, include
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('clientes/', include('clientes.urls')),
    path('agenda/', include('agenda.urls')),
    path('procedimentos/', include('procedimentos.urls')),
    path('financeiro/', include('financeiro.urls')),
]
