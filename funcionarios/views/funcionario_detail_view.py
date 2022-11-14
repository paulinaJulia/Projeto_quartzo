from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ..models import Funcionario


class FuncionarioDetailView(LoginRequiredMixin, DetailView):
    model = Funcionario

    template_name = 'funcionario_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
