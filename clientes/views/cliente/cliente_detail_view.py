from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ...models import Usuario


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Usuario

    template_name = 'clientes/cliente_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
