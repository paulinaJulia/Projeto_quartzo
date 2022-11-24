from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ..models import Imovel
from financeiro.models import Contrato


class ImovelListView(LoginRequiredMixin, ListView):
    model = Imovel
    template_name = 'imovel_list_view.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
       
        if self.request.GET.get("myImoveis"):
            print('...')
            if user.nivel == 'Usuario':
                imoveis = []
                for contrato in Contrato.objects.filter(funcionario__id=user.id):
                    imoveis.append(contrato.imovel.id)
                context['object_list'] = Imovel.objects.filter(
                    id__in=imoveis)
            elif user.nivel == 'Funcionario':
                imoveis = []
                for contrato in Contrato.objects.filter(funcionario__id=user.id):
                    imoveis.append(contrato.imovel.id) 
                context['object_list'] =  Imovel.objects.filter(
                    id__in=imoveis)
            
        return context
