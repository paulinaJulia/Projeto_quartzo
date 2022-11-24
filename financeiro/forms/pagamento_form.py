from django import forms

from financeiro.models import Pagamento


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento

        fields = ['total_parcelas', 'forma_pagamento']
