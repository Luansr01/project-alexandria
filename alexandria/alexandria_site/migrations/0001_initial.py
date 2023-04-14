# Generated by Django 4.1.7 on 2023-04-13 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo da Página')),
                ('content', models.TextField(verbose_name='Conteúdo')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='Sobre')),
                ('logo', models.ImageField(blank=True, upload_to='', verbose_name='Logo')),
                ('site', models.URLField(blank=True, verbose_name='Site')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Titulo')),
                ('slug', models.SlugField(max_length=20, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Conteúdo do Post')),
                ('images', models.ImageField(blank=True, upload_to='', verbose_name='Imagem')),
                ('date_posted', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('date_edited', models.DateField(auto_now=True, verbose_name='Data da Ultima Edição')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome do Projeto')),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='Estado')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('slug', models.SlugField(help_text='<small>Nome do Projeto em minúsculo mudando os espaços para hífens.<br>Ex: projeto-somar, projeto-alexandria, etc.', verbose_name='Slug')),
                ('about', models.TextField(verbose_name='Sobre o Projeto')),
                ('cause', models.CharField(blank=True, max_length=30, verbose_name='Causa')),
                ('ODS', models.ManyToManyField(to='alexandria_site.objective')),
                ('partners', models.ManyToManyField(to='alexandria_site.partner')),
            ],
        ),
    ]
