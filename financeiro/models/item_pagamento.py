from django.db import models
from imoveis.models import Imovel
from clientes.models import Usuario
from core.models import BaseModel

"""base model para pegar a data do pagamento criado"""
class ItemPagamento(BaseModel):
         

    imovel = models.ForeignKey(
        Imovel,
        on_delete=models.PROTECT
    )

    cliente = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='Cliente'
    )

    valor_parcela= models.FloatField(
        verbose_name='Valor da Parcela ',
        blank=True, null=True,
    )

    date_vencimento = None

    numero = models.IntegerField(
        verbose_name='Numero',
        blank=True, null=True,
    )

    STATUS= (
        ('aprovado',  'aprovado'),
        ('pendente',  'pendente'),
        ('vencido', 'vencido'),
    )

    status = models.CharField(
        blank=True,
        null=True,
        verbose_name="Status do pagamento",
        max_length=500,
        default= 'pendente',
        choices= STATUS
    )


    def __str__(self):
        return self.status

    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Item pagamento'
        verbose_name_plural = 'itens pagamento'
