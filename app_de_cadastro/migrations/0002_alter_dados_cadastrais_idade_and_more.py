# Generated by Django 5.0.4 on 2024-05-06 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_de_cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_cadastrais',
            name='idade',
            field=models.IntegerField(verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='dados_cadastrais',
            name='nome',
            field=models.CharField(max_length=150, verbose_name='Nome Completo'),
        ),
    ]