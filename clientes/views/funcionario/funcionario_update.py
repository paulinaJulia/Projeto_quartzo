from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from ...forms import FuncionarioForm
from ...models import Usuario


class FuncionarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    #fields = '__all__'
    form_class = FuncionarioForm
    template_name = 'funcionarios/funcionario_update.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus(
            'funcionario_detail',
            url_params= [self.kwargs.get('pk')],
            get_params= {
                'mensagem_toastify':'Funcionario editado com sucesso!'
            },
            just_uri=True,
        )

