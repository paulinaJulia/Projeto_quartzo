from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from ..forms import FuncionarioForm
from ..models import Funcionario


class FuncionarioCreateView(LoginRequiredMixin, CreateView):
    model = Funcionario

    form_class = FuncionarioForm

    template_name = 'funcionario_create_view.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            'funcionario_list',
            get_params= {
                'mensagem_toastify':'Funcionario adicionado com sucesso!'
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)



        return context 