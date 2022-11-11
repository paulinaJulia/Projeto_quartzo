from django.db import models
from imoveis.models import Imovel
from clientes.models import Cliente
from funcionarios.models import Funcionario
from .pagamento import Pagamento

class Contrato(models.Model):

    imovel = models.ForeignKey(
        Imovel,
        on_delete=models.PROTECT
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT
    )

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT
    )

    inicio = models.DateTimeField(
        verbose_name='Data de Inicio',
        null=True, 
        blank=True
    )

    termino = models.DateTimeField(
        verbose_name='Data de termino',
        null=True, 
        blank=True
    )

    data_vencimento = models.DateField(
        verbose_name='Data Vencimento',
        blank=True, null=True,
    )

    SITUACAO = (
        ('Aberto',  'Aberto'),
        ('Vencido',  'Vencido'),
        ('Encerrado',  'Encerrado'),

    )

    situacao = models.CharField(
        blank=True,
        null=True,
        verbose_name="Situação",
        max_length=500,
        default= 'Aberto',
        choices= SITUACAO
    )

    pagamento = models.ForeignKey(
        Pagamento,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.situacao

    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
