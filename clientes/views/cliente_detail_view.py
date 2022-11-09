from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ..models import Cliente


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente

    template_name = 'cliente_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
