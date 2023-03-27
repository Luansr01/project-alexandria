# Generated by Django 4.1.7 on 2023-03-26 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alexandria_site', '0002_rename_partners_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_cause',
            field=models.CharField(default='N/A', max_length=30, verbose_name='Causa'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_about',
            field=models.TextField(verbose_name='Sobre o Projeto'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_city',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=50, verbose_name='Nome do Projeto'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_slug',
            field=models.SlugField(help_text='<small>Nome do Projeto em minúsculo mudando os espaços para hífens.<br>Ex: projeto-somar, projeto-alexandria, etc.', verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='Estado'),
        ),
    ]
