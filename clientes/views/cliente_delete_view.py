from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

from ..models import Cliente


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente

    template_name = 'cliente_delete.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus(
            'cliente_list',
            get_params= {
                'mensagem_toastify':'Cliente deletado com sucesso!'
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
