from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ..models import Imovel


class ImovelDetailView(LoginRequiredMixin, DetailView):
    model = Imovel

    template_name = 'imovel_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
