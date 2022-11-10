from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

from ..models import Imovel


class ImovelDeleteView(LoginRequiredMixin, DeleteView):
    model = Imovel

    template_name = 'imovel_delete_view.html'
#olhar dealhes 

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus(
            'imovel_list',
            get_params= {
                'mensagem_toastify':'Imovel deletado com sucesso!'
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context