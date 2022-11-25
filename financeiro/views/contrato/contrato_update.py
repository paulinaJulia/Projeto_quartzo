from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from clientes.models.usuario import Usuario

from ...models import Contrato
from ...forms import ContratoForm

class ContratoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contrato
    form_class = ContratoForm
    #fields = '__all__'
    template_name = 'contrato_update.html'

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus
        return reverse_lazy_plus(
            'contrato_detail',
            url_params= [self.kwargs.get('pk')],
            get_params= {
                'mensagem_toastify':'Contrato editado com sucesso!'
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.get('form').fields['cliente'].queryset = Usuario.objects.filter(
            nivel='Usuario')

        return context