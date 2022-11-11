from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

from ...models import Contrato


class ContratoDeleteView(LoginRequiredMixin, DeleteView):
    model = Contrato

    template_name = 'contrato_delete.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus(
            'contrato_list',
            get_params= {
                'mensagem_toastify':'Contrato deletado com sucesso!'
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
