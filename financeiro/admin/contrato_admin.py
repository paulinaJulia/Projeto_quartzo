from django.contrib import admin

from ..models import Contrato


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'imovel',
        'cliente',
        'inicio',
        'termino',
        'data_vencimento',
    ]

    search_fields = [
        'id',
        'imovel',
        'cliente',
        'inicio',
        'termino',
        'data_vencimento',
    ]

   