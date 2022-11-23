from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from ..forms import ImovelForm
from ..models import Imovel

from django.contrib.auth.mixins import PermissionRequiredMixin
class ImovelCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'imoveis.add_imovel',
    model = Imovel

    form_class = ImovelForm

    template_name = 'imovel_create_view.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            'imovel_list',
            get_params= {
                'mensagem_toastify':'Imovel adicionado com sucesso!'
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)



        return context 
