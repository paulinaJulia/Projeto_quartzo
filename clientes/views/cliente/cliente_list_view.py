from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ...models import Usuario


class ClienteListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'clientes/cliente_list_view.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Usuario.objects.filter(nivel='Usuario')
    

        return context
