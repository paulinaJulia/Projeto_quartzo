from django.db import models
from .usuario import Usuario
from imoveis.models import Imovel

class Favorito(models.Model):
 
    usuario =  models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT
    )

    imovel =  models.ForeignKey(
        Imovel,
        on_delete=models.PROTECT
    )

    class Meta:
        app_label = 'clientes'
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
