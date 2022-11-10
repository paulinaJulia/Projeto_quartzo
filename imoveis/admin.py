from django.contrib import admin

from .models import Imovel

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'rua',
        'bairro',
        'cidade',
        'valor',
    ]

    search_fields = [
        'id',
        'rua',
        'bairro',
        'cidade',
        'valor',
    ]