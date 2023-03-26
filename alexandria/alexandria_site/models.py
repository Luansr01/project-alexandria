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

class Partner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Objective(models.Model):
    name = models.CharField(max_length=60) 

    def __str__(self):
        return self.name

class Project(models.Model):
    project_name = models.CharField("Nome do Projeto", max_length=50)
    project_state = models.CharField("Estado", max_length=2, choices=STATE_CHOICES)
    project_city = models.CharField("Cidade", max_length=50)
    project_slug = models.SlugField("Slug", help_text="<small>Nome do Projeto em minúsculo mudando os espaços para hífens.<br>Ex: projeto-somar, projeto-alexandria, etc.", max_length=50)

    project_about = models.TextField("Sobre o Projeto")

    ODS = models.ManyToManyField(Objective)
    project_cause = models.CharField("Causa", max_length=30, default="N/A")
    project_partners = models.ManyToManyField(Partner)

    def __str__(self):
        return self.project_name
    