from django.db import models
from .cliente import Cliente
from imoveis.models import Imovel

class Favorito(models.Model):
 
    usuario =  models.ForeignKey(
        Cliente,
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
