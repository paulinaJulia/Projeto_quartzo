from django.db import models

# Create your models here.
from django.db import models

#cso queira deixar pegar mais de uma imagem, mas tem que ver como o formulario no front funciona
"""class ImagemImovel(models.Model):
     imagem = models.ImageField(
        upload_to='static/images/',
        blank=True,
        null=True,
    )
"""
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

    imagem = models.ImageField(
        upload_to='static/images/',
        blank=True,
        null=True,
    )

    descricao = models.CharField(
        verbose_name='Descrição do imovel',
        max_length=500,
        blank=True,
        null=True,
        default=None
    )



     
    def __str__(self):
        return self.categoria

    class Meta:
        app_label = 'imoveis'
        verbose_name = 'imovel'
        verbose_name_plural = 'imoveis'


