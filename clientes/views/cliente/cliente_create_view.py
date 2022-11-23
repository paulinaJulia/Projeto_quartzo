from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from functions_globais.utils.create_user import create_user

from ...forms import UsuarioForm
from ...models import Usuario

from django.contrib.auth.mixins import PermissionRequiredMixin

class ClienteCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'clientes.add_cliente',
    model = Usuario

    form_class = UsuarioForm

    template_name = 'clientes/cliente_create.html'

    def form_valid(self, form):
        form = super().form_valid(form)
        create_user(self.object, 'Usuario')
        return form

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        print("success")
        return reverse_lazy_plus(
            'cliente_list',
            get_params= {
                'mensagem_toastify':'Cliente adicionado com sucesso!'
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        return context 