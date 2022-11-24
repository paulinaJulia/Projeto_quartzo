from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from financeiro.models.contrato import Contrato

from financeiro.models.item_pagamento import ItemPagamento
from functions_globais.utils.listar_data import dates

from ...forms import PagamentoForm
from ...models import Pagamento


class PagamentoCreateView(LoginRequiredMixin, CreateView):
    model = Pagamento

    form_class = PagamentoForm

    template_name = 'pagamento/pagamento_create.html'

    def form_valid(self, form):
        form = super().form_valid(form)
        id = self.request.GET.get('id')
        contrato = get_object_or_404(Contrato, pk=id)
        print("contrato", contrato.id)
        self.object.cliente = contrato.cliente
        self.object.valor = contrato.imovel.valor
        self.object.save()
        contrato.pagamento = self.object
        contrato.save()
        
        def popularItens(pagamento, imovel, cliente):
            valor_parcela = pagamento.valor / pagamento.total_parcelas
            datas = dates(datetime.now() - timedelta(hours=3), pagamento.total_parcelas)
            for i in range(0, pagamento.total_parcelas):
                item = ItemPagamento()
                item.numero = i + 1
                item.data_vencimento = datas[i]
                item.imovel = imovel
                item.cliente = cliente
                item.valor_parcela = valor_parcela
                item.save()
                pagamento.items.add(item)

        popularItens(self.object, contrato.imovel, contrato.cliente)
        return form


    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus('contrato_list', just_uri=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.GET.get('id')
        contrato = get_object_or_404(Contrato, pk=id)
        context['valor_contrato'] = contrato.imovel.valor
        return context
