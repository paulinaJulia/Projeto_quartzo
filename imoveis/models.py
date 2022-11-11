from django.db import models

# Create your models here.
from django.db import models


class Imovel(models.Model):

    area = models.CharField(
        verbose_name='Area',
        max_length=100
    )

    rua = models.CharField(
        verbose_name='Rua',
        max_length=100
    )

    bairro = models.CharField(
        verbose_name='Bairro',
        max_length=100
    )

    cidade = models.CharField(
        verbose_name='Cidade',
        max_length=100
    )

    numero = models.IntegerField(
        verbose_name='Numero',
        blank=True, null=True,
    )

    valor= models.FloatField(
        verbose_name='Valor',
        blank=True, null=True,
    )

    CATEGORIA = [
        ('Casa', 'Casa'),
        ('Apartamento', 'Apartamento'),
        ('Terreno', 'Terreno'),
        ('Predio comercial', 'Predio comercial'),
    ]

    categoria = models.CharField(
        verbose_name='Categoria',
        max_length=100,
        choices = CATEGORIA,
        blank = False, null = True
    )
     
    def __str__(self):
        return self.categoria

    class Meta:
        app_label = 'imoveis'
        verbose_name = 'imovel'
        verbose_name_plural = 'imoveis'
