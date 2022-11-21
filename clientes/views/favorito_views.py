from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from ..models import Favorito


class FavoritoCreateView(LoginRequiredMixin, CreateView):
    model = Favorito

    def get_success_url(self):
        from functions_globais.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            'home',
            get_params= {
                'mensagem_toastify':'Favoritado com sucesso!'
            },
            just_uri=True,
        )

        

    def get_context_data(self, **kwargs):
        self.request.user
        context = super().get_context_data(**kwargs)
         


        return context 