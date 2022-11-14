from django.db import models


class Cliente (models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do Cliente'
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=18,
        blank=True, null=True
    )

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=16,
        blank=True, null=True
    )

    rua = models.CharField(
        verbose_name='Rua',
        max_length=16,
        blank=True, null=True 
    )

    cidade = models.CharField(
        verbose_name='Cidade',
        max_length=16,
        blank=True, null=True
    )

    bairro = models.CharField(
        verbose_name='Bairro',
        max_length=16,
        blank=True, null=True
    )

    numero_casa = models.IntegerField(
        verbose_name='Numero da Casa',
        blank=True, null=True,
    )

    """email = models.EmailField(
        verbose_name='E-mail',
    )"""

    email = models.CharField(
        verbose_name='Email',
        max_length=16,
        blank=True,
        null=True,
    )

    senha = models.CharField(
        verbose_name='Senha',
        max_length=16,
        blank=True, null=True
    )
