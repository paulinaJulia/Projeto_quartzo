from django.contrib import admin

from ..models import Pagamento


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'valor',
        'forma_pagamento',
    ]

    search_fields = [
        'id',
        'valor',
        'forma_pagamento',
    ]

