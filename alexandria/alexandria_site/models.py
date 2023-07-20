from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator


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


    date_posted = models.DateField("Data de Criação", auto_now_add=True)
    date_edited = models.DateField("Data da Ultima Edição", auto_now=True)

    def __str__(self):
        return self.title

class Partner(models.Model):
    def projects(self):
        return self.project_set.all().count()

    class Meta:
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'

    name = models.CharField("Nome", max_length=50)
    about = models.TextField("Sobre", max_length=500, blank=True)
    logo = models.ImageField("Logo", blank=True)
    site = models.URLField("Site", blank=True)

    def __str__(self):
        return self.name

class Objective(models.Model):
    def projects(self):
        return self.project_set.all().count()

    class Meta:
        verbose_name = 'ODS'
        verbose_name_plural = 'Objetivos'

    name = models.CharField(max_length=60) 

    icon = models.ImageField("Icone", upload_to="icons", blank=True)

    def __str__(self):
        return self.name



class Project(models.Model):

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


    name = models.CharField("Nome do Projeto", max_length=50)
    state = models.CharField("Estado", max_length=2, choices=STATE_CHOICES)
    city = models.CharField("Cidade", max_length=50)

    about = models.TextField("Sobre o Projeto")

    ODS = models.ManyToManyField(Objective)
    cause = models.CharField("Causa", max_length=60, blank=True)
    partners = models.ManyToManyField(Partner, verbose_name="Parceiros")

    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.name

    def ods(self):
        odss = self.ODS.all()
        if odss.count() > 1:
            odss = ", ".join(list([x.name for x in self.ODS.all()]))
        else:
            odss = self.ODS.all()[0]
    
        return odss

    def folder_name(self, name):
        return f'{self.name}_project_media/{name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    

for i in range(6):
    Project.add_to_class(f'image_{i+1}', models.ImageField("Imagem", upload_to=Project.folder_name, blank=True))

Project.add_to_class('video', models.FileField("Video", upload_to=Project.folder_name, blank=True, validators=[FileExtensionValidator(allowed_extensions=['mp4'])]))

    