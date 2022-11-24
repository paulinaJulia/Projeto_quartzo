from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from financeiro.models import ItemPagamento
from functions_globais.utils.listar_data import dates

from ...forms import ContratoForm
from ...models import Contrato
from clientes.models import Usuario

class ContratoCreateView(LoginRequiredMixin, CreateView):
    model = Contrato

    form_class = ContratoForm

    template_name = 'contrato_create.html'

    def form_valid(self, form): 
        form = super().form_valid(form)
        self.object.funcionario = self.request.user
        self.object.save()
        return form

    def get_success_url(self):        
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus(
            'pagamento_create',
            get_params= {
                'id': self.object.id
            },
            just_uri=True,
        )   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.get('form').fields['cliente'].queryset = Usuario.objects.filter(
            nivel='Usuario')

        return context
    