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
    def folder_name(self, postname):
        return f'{self.title}_blog_images/{postname}'


    title = models.CharField("Titulo", max_length=60)
    slug = models.SlugField("Slug", max_length=20)

    content = models.TextField("Conteúdo do Post")

    image = models.ImageField("Imagem", upload_to=folder_name, blank=True)

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

    icon = models.ImageField("Icone", upload_to="icons", blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    def folder_name(self, name):
        return f'{self.name}_project_images/{name}'

    def gen_slug(self, name):
        return self.name.lower().replace(" ", "-")

    name = models.CharField("Nome do Projeto", max_length=50)
    state = models.CharField("Estado", max_length=2, choices=STATE_CHOICES)
    city = models.CharField("Cidade", max_length=50)

    about = models.TextField("Sobre o Projeto")

    ODS = models.ManyToManyField(Objective)
    cause = models.CharField("Causa", max_length=30, blank=True)
    partners = models.ManyToManyField(Partner, verbose_name="Parceiros")

    def __str__(self):
        return self.name
    

for i in range(3):
    Project.add_to_class(f'image_{i+1}', models.ImageField("Imagem", upload_to=Project.folder_name, blank=True))

Project.add_to_class('slug', models.SlugField("Slug", editable=False, blank=False, default=Project.gen_slug))


class Page(models.Model):
    title = models.CharField("Titulo da Página", max_length=50)
    content = models.TextField("Conteúdo")
    
    def __str__(self):
        return self.title
    

    