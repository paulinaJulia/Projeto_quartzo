from django.db import models
from django.contrib.auth.models import AbstractUser

from functions_globais.utils.create_permissions import create_permision, create_permissions

class Usuario (AbstractUser):

    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do Usuario',
        blank=True,
        null=True,
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=18,
        blank=True, null=True
    )

    imagem = models.ImageField(
        upload_to='static/images/',
        blank=True,
        null=True,
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

    NIVEL = [
        ('Funcionario', 'Funcionario'),
        ('Gerente', 'Gerente'),
        ('Usuario', 'Usuario'),
    ]

    nivel = models.CharField(
        verbose_name='Nivel',
        max_length=100,
        choices = NIVEL,
        blank = False, null = True
    )

    def __str__(self):
        return self.nome
    
    def save_permissions(self):        
        if self.nivel == 'Funcionario':
            def call_permissions(ct):
                items = [ {
                    'codename': 'add_imovel',
                    'name': 'Add imovel'
                }, 
                {
                    'codename': 'add_cliente',
                    'name': 'Add cliente'
                }
                ]
                permissions = []
                for item in items:
                    permissions.append(create_permision(item['codename'], item['name'], ct))
                return permissions

            create_permissions(self, call_permissions)
        elif self.nivel == 'Usuario':
            def call_permissions(ct):
                items = [ {
                    'codename': 'add_imovel',
                    'name': 'Add imovel'
                },
                ]
                permissions = []
                for item in items:
                    permissions.append(create_permision(item['codename'], item['name'], ct))
                return permissions
                
            create_permissions(self, call_permissions)

    class Meta:
        app_label = 'clientes'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
