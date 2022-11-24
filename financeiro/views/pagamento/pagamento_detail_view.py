from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ...models import Pagamento


class PagamentoDetailView(LoginRequiredMixin, DetailView):
    model = Pagamento

    template_name = 'pagamento/pagamento_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
