from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from ..models import Cliente


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente_update.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus(
            'cliente_detail',
            url_params= [self.kwargs.get('pk')],
            get_params= {
                'mensagem_toastify':'Cliente editado com sucesso!'
            },
            just_uri=True,
        )

