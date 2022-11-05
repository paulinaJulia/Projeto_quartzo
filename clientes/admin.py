from django.contrib import admin

from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'cpf',
    ]

    search_fields = [
        'id',
        'nome',
        'cpf',
    ]
