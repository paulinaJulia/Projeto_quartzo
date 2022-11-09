from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from ..forms import ClienteForm
from ..models import Cliente


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente

    form_class = ClienteForm

    template_name = 'cliente_create.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            'cliente_list',
            get_params= {
                'mensagem_toastify':'Cliente adicionado com sucesso!'
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)



        return context 