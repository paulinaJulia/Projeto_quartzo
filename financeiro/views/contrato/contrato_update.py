from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from ...models import Contrato


class ContratoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contrato
    fields = '__all__'
    template_name = 'contrato_update.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus(
            'contrato_detail',
            url_params= [self.kwargs.get('pk')],
            get_params= {
                'mensagem_toastify':'Contrato editado com sucesso!'
            },
            just_uri=True,
        )

