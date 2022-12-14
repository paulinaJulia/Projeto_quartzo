from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ...models import Contrato


class ContratoDetailView(LoginRequiredMixin, DetailView):
    model = Contrato

    template_name = 'contrato_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
