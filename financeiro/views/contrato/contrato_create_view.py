from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from ...forms import ContratoForm
from ...models import Contrato


class ContratoCreateView(LoginRequiredMixin, CreateView):
    model = Contrato

    form_class = ContratoForm

    template_name = 'contrato_create.html'

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



        return context 