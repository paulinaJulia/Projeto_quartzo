from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from ..models import Imovel


class ImovelUpdateView(LoginRequiredMixin, UpdateView):
    model = Imovel
    fields = '__all__'
    template_name = 'imovel_update.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus(
            'imovel_detail',
            url_params= [self.kwargs.get('pk')],
            get_params= {
                'mensagem_toastify':'Imovel editado com sucesso!'
            },
            just_uri=True,
        )