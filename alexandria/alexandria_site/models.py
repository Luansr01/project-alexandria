from django.db import models

STATE_CHOICES = ( 
	('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), 
	('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), 
	('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), 
	('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), 
	('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), 
	('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), 
	('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
	('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), 
	('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), 
	('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)

# MODELS

class Post(models.Model):
    title = models.CharField("Titulo", max_length=60)
    slug = models.SlugField("Slug", max_length=20)

    content = models.TextField("Conteúdo do Post")

    images = models.ImageField("Imagem")

    date_posted = models.DateField("Data de Criação", auto_now_add=True)
    date_edited = models.DateField("Data da Ultima Edição", auto_now=True)

    def __str__(self):
        return self.title

class Partner(models.Model):
    name = models.CharField("Nome", max_length=50)
    about = models.TextField("Sobre", max_length=500, blank=True)
    logo = models.ImageField("Logo", blank=True)
    site = models.URLField("Site", blank=True)

    def __str__(self):
        return self.name

class Objective(models.Model):
    name = models.CharField(max_length=60) 

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField("Nome do Projeto", max_length=50)
    state = models.CharField("Estado", max_length=2, choices=STATE_CHOICES)
    city = models.CharField("Cidade", max_length=50)
    slug = models.SlugField("Slug", help_text="<small>Nome do Projeto em minúsculo mudando os espaços para hífens.<br>Ex: projeto-somar, projeto-alexandria, etc.", max_length=50)

    about = models.TextField("Sobre o Projeto")

    ODS = models.ManyToManyField(Objective)
    cause = models.CharField("Causa", max_length=30, blank=True)
    partners = models.ManyToManyField(Partner)

    def __str__(self):
        return self.project_name
    

    