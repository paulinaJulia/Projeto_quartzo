from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from financeiro.models import item_pagamento
from functions_globais.utils.listar_data import days_of_month

from ...forms import ContratoForm
from ...models import Contrato
from clientes.models import Usuario

class ContratoCreateView(LoginRequiredMixin, CreateView):
    model = Contrato

    form_class = ContratoForm

    template_name = 'contrato_create.html'

    def form_valid(self, form):
        def popularItens(total_parcelas, pagamento, imovel, cliente):
            datas = days_of_month()
            for i in range(0, total_parcelas):
                item = item_pagamento()
                item.numero = i + 1
                item.date_vencimento = datas[i]
                item.imovel = imovel
                item.cliente = cliente
                item.save()
                pagamento.items.append(item)

        popularItens(self.total_parcelas, self.pagamento, self.imovel, self.cliente)
        return super().form_valid(form)

    def get_success_url(self):        

        from functions_globais.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            'contrato_list',
            get_params= {
                'mensagem_toastify':'Contrato adicionado com sucesso!'
            },
            just_uri=True,
        )   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.get('form').fields['cliente'].queryset = Usuario.objects.filter(
            nivel='Usuario')

        return context
    