# Generated by Django 4.1.3 on 2022-11-23 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AddField(
            model_name='usuario',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
