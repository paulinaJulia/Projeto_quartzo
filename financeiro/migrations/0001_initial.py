# Generated by Django 4.1.3 on 2022-11-22 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imoveis', '0006_imovel_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Valor R$')),
                ('forma_pagamento', models.CharField(blank=True, choices=[('Dinheiro', 'Dinheiro'), ('Cartão', 'Cartão'), ('Boleto', 'Boleto'), ('Pix', 'Pix')], default='Aberto', max_length=500, null=True, verbose_name='Forma de Pagamento')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contrato', models.CharField(choices=[('Compra', 'Compra'), ('Venda', 'Venda'), ('Aluga', 'Aluga')], max_length=100, null=True, verbose_name='Categoria')),
                ('inicio', models.DateTimeField(blank=True, null=True, verbose_name='Data de Inicio')),
                ('termino', models.DateTimeField(blank=True, null=True, verbose_name='Data de termino')),
                ('data_vencimento', models.DateField(blank=True, null=True, verbose_name='Data Vencimento')),
                ('situacao', models.CharField(blank=True, choices=[('Aberto', 'Aberto'), ('Vencido', 'Vencido'), ('Encerrado', 'Encerrado')], default='Aberto', max_length=500, null=True, verbose_name='Situação')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Cliente', to=settings.AUTH_USER_MODEL)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Funcionario', to=settings.AUTH_USER_MODEL)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='imoveis.imovel')),
                ('pagamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='financeiro.pagamento')),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contratos',
            },
        ),
    ]
