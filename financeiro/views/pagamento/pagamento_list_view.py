from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from ...models import Pagamento


class PagamentoListView(LoginRequiredMixin, ListView):
    model = Pagamento
    template_name = 'pagamento/pagamento_list_view.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Pagamento.objects.filter(
            cliente__id=self.request.user.id)
        return context
