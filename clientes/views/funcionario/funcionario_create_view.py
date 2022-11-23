from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from functions_globais.utils.create_user import create_user

from ...forms import FuncionarioForm
from ...models import Usuario

from django.contrib.auth.mixins import PermissionRequiredMixin

class FuncionarioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'clientes.add_funcionario',
    # Or multiple of permissions:
    #permission_required = ('polls.view_choice', 'polls.change_choice')

    model = Usuario

    form_class = FuncionarioForm

    template_name = 'funcionarios/funcionario_create_view.html'

    def form_valid(self, form):
        form = super().form_valid(form)
        create_user(self.object, 'Funcionario') 
        return form


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