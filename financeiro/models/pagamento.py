from django.db import models


class Pagamento(models.Model):

    valor = models.DecimalField(
        verbose_name='Valor R$',
        decimal_places=2,
        max_digits=30,
        blank=True, null=True,
    )

    FORMA_PAGAMENTO= (
        ('Dinheiro',  'Dinheiro'),
        ('Cartão',  'Cartão'),
        ('Boleto', 'Boleto'),
        ('Pix',  'Pix'),

    )

    forma_pagamento = models.CharField(
        blank=True,
        null=True,
        verbose_name="Forma de Pagamento",
        max_length=500,
        default= 'Aberto',
        choices= FORMA_PAGAMENTO
    )

    def __str__(self):
        return self.forma_pagamento

    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
