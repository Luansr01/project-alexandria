from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from colorfield.fields import ColorField


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

CITY_CHOICES =  (('Aceguá', 'Aceguá'), ('Água Santa', 'Água Santa'), ('Agudo', 'Agudo'), ('Ajuricaba', 'Ajuricaba'), ('Alecrim', 'Alecrim'), ('Alegrete', 'Alegrete'), ('Almirante Tamandaré Do Sul', 'Almirante Tamandaré Do Sul'), ('Alpestre', 'Alpestre'), ('Alto Alegre', 'Alto Alegre'), ('Alvorada', 'Alvorada'), ('Ametista Do Sul', 'Ametista Do Sul'), ('André Da Rocha', 'André Da Rocha'), ('Anta Gorda', 'Anta Gorda'), ('Antônio Prado', 'Antônio Prado'), ('Aratiba', 'Aratiba'), ('Arroio Do Meio', 'Arroio Do Meio'), ('Arroio Do Sal', 'Arroio Do Sal'), ('Arroio Do Tigre', 'Arroio Do Tigre'), ('Arroio Grande', 'Arroio Grande'), ('Arvorezinha', 'Arvorezinha'), ('Augusto Pestana', 'Augusto Pestana'), ('Bagé', 'Bagé'), ('Balneário Pinhal', 'Balneário Pinhal'), ('Barão De Cotegipe', 'Barão De Cotegipe'), ('Barão Do Triunfo', 'Barão Do Triunfo'), ('Barracão', 'Barracão'), ('Barra Do Quaraí', 'Barra Do Quaraí'), ('Barra Do Ribeiro', 'Barra Do Ribeiro'), ('Barra Funda', 'Barra Funda'), ('Barros Cassal', 'Barros Cassal'), ('Bento Gonçalves', 'Bento Gonçalves'), ('Boa Vista Das Missões', 'Boa Vista Das Missões'), ('Boa Vista Do Buricá', 'Boa Vista Do Buricá'), ('Boa Vista Do Cadeado', 'Boa Vista Do Cadeado'), ('Boa Vista Do Sul', 'Boa Vista Do Sul'), ('Bom Jesus', 'Bom Jesus'), ('Bom Princípio', 'Bom Princípio'), ('Bom Retiro Do Sul', 'Bom Retiro Do Sul'), ('Boqueirão Do Leão', 'Boqueirão Do Leão'), ('Braga', 'Braga'), ('Brochier', 'Brochier'), ('Butiá', 'Butiá'), ('Caçapava Do Sul', 'Caçapava Do Sul'), ('Cacequi', 'Cacequi'), ('Cachoeira Do Sul', 'Cachoeira Do Sul'), ('Cachoeirinha', 'Cachoeirinha'), ('Cacique Doble', 'Cacique Doble'), ('Caibaté', 'Caibaté'), ('Caiçara', 'Caiçara'), ('Camaquã', 'Camaquã'), ('Camargo', 'Camargo'), ('Cambará Do Sul', 'Cambará Do Sul'), ('Campestre Da Serra', 'Campestre Da Serra'), ('Campinas Do Sul', 'Campinas Do Sul'), ('Campo Bom', 'Campo Bom'), ('Campos Borges', 'Campos Borges'), ('Candelária', 'Candelária'), ('Cândido Godói', 'Cândido Godói'), ('Candiota', 'Candiota'), ('Canela', 'Canela'), ('Canguçu', 'Canguçu'), ('Canoas', 'Canoas'), ('Capão Bonito Do Sul', 'Capão Bonito Do Sul'), ('Capão Da Canoa', 'Capão Da Canoa'), ('Capão Do Leão', 'Capão Do Leão'), ('Carazinho', 'Carazinho'), ('Carlos Barbosa', 'Carlos Barbosa'), ('Casca', 'Casca'), ('Caseiros', 'Caseiros'), ('Caxias Do Sul', 'Caxias Do Sul'), ('Cerro Grande', 'Cerro Grande'), ('Cerro Largo', 'Cerro Largo'), ('Chapada', 'Chapada'), ('Charqueadas', 'Charqueadas'), ('Charrua', 'Charrua'), ('Chiapetta', 'Chiapetta'), ('Ciríaco', 'Ciríaco'), ('Colorado', 'Colorado'), ('Condor', 'Condor'), ('Constantina', 'Constantina'), ('Coqueiros Do Sul', 'Coqueiros Do Sul'), ('Coronel Barros', 'Coronel Barros'), ('Coronel Bicaco', 'Coronel Bicaco'), ('Coronel Pilar', 'Coronel Pilar'), ('Cotiporã', 'Cotiporã'), ('Crissiumal', 'Crissiumal'), ('Cristal', 'Cristal'), ('Cristal Do Sul', 'Cristal Do Sul'), ('Cruz Alta', 'Cruz Alta'), ('Cruzaltense', 'Cruzaltense'), ('Cruzeiro Do Sul', 'Cruzeiro Do Sul'), ('David Canabarro', 'David Canabarro'), ('Derrubadas', 'Derrubadas'), ('Dois Irmãos', 'Dois Irmãos'), ('Dom Feliciano', 'Dom Feliciano'), ('Dom Pedro De Alcântara', 'Dom Pedro De Alcântara'), ('Dom Pedrito', 'Dom Pedrito'), ('Dona Francisca', 'Dona Francisca'), ('Eldorado Do Sul', 'Eldorado Do Sul'), ('Encantado', 'Encantado'), ('Encruzilhada Do Sul', 'Encruzilhada Do Sul'), ('Engenho Velho', 'Engenho Velho'), ('Entre-ijuís', 'Entre-ijuís'), ('Entre Rios Do Sul', 'Entre Rios Do Sul'), ('Erechim', 'Erechim'), ('Ernestina', 'Ernestina'), ('Erval Grande', 'Erval Grande'), ('Erval Seco', 'Erval Seco'), ('Esmeralda', 'Esmeralda'), ('Espumoso', 'Espumoso'), ('Estância Velha', 'Estância Velha'), ('Esteio', 'Esteio'), ('Estrela', 'Estrela'), ('Fagundes Varela', 'Fagundes Varela'), ('Farroupilha', 'Farroupilha'), ('Faxinal Do Soturno', 'Faxinal Do Soturno'), ('Fazenda Vilanova', 'Fazenda Vilanova'), ('Feliz', 'Feliz'), ('Flores Da Cunha', 'Flores Da Cunha'), ('Fontoura Xavier', 'Fontoura Xavier'), ('Forquetinha', 'Forquetinha'), ('Fortaleza Dos Valos', 'Fortaleza Dos Valos'), ('Frederico Westphalen', 'Frederico Westphalen'), ('Garibaldi', 'Garibaldi'), ('General Câmara', 'General Câmara'), ('Gentil', 'Gentil'), ('Getúlio Vargas', 'Getúlio Vargas'), ('Giruá', 'Giruá'), ('Gramado', 'Gramado'), ('Gramado Xavier', 'Gramado Xavier'), ('Gravataí', 'Gravataí'), ('Guabiju', 'Guabiju'), ('Guaíba', 'Guaíba'), ('Guaporé', 'Guaporé'), ('Guarani Das Missões', 'Guarani Das Missões'), ('Horizontina', 'Horizontina'), ('Humaitá', 'Humaitá'), ('Ibiaçá', 'Ibiaçá'), ('Ibiraiaras', 'Ibiraiaras'), ('Ibirapuitã', 'Ibirapuitã'), ('Ibirubá', 'Ibirubá'), ('Igrejinha', 'Igrejinha'), ('Ijuí', 'Ijuí'), ('Ilópolis', 'Ilópolis'), ('Imbé', 'Imbé'), ('Imigrante', 'Imigrante'), ('Independência', 'Independência'), ('Ipê', 'Ipê'), ('Iraí', 'Iraí'), ('Itapuca', 'Itapuca'), ('Itaqui', 'Itaqui'), ('Itatiba Do Sul', 'Itatiba Do Sul'), ('Ivoti', 'Ivoti'), ('Jaboticaba', 'Jaboticaba'), ('Jaguarão', 'Jaguarão'), ('Jaguari', 'Jaguari'), ('Jaquirana', 'Jaquirana'), ('Jóia', 'Jóia'), ('Júlio De Castilhos', 'Júlio De Castilhos'), ('Lagoão', 'Lagoão'), ('Lagoa Dos Três Cantos', 'Lagoa Dos Três Cantos'), ('Lagoa Vermelha', 'Lagoa Vermelha'), ('Lajeado', 'Lajeado'), ('Lavras Do Sul', 'Lavras Do Sul'), ('Liberato Salzano', 'Liberato Salzano'), ('Linha Nova', 'Linha Nova'), ('Machadinho', 'Machadinho'), ('Manoel Viana', 'Manoel Viana'), ('Maratá', 'Maratá'), ('Marau', 'Marau'), ('Marcelino Ramos', 'Marcelino Ramos'), ('Marques De Souza', 'Marques De Souza'), ('Mato Castelhano', 'Mato Castelhano'), ('Mato Leitão', 'Mato Leitão'), ('Maximiliano De Almeida', 'Maximiliano De Almeida'), ('Minas Do Leão', 'Minas Do Leão'), ('Miraguaí', 'Miraguaí'), ('Montauri', 'Montauri'), ('Monte Alegre Dos Campos', 'Monte Alegre Dos Campos'), ('Monte Belo Do Sul', 'Monte Belo Do Sul'), ('Montenegro', 'Montenegro'), ('Mormaço', 'Mormaço'), ('Muçum', 'Muçum'), ('Muitos Capões', 'Muitos Capões'), ('Muliterno', 'Muliterno'), ('Nicolau Vergueiro', 'Nicolau Vergueiro'), ('Nonoai', 'Nonoai'), ('Nova Alvorada', 'Nova Alvorada'), ('Nova Araçá', 'Nova Araçá'), ('Nova Bassano', 'Nova Bassano'), ('Nova Boa Vista', 'Nova Boa Vista'), ('Nova Bréscia', 'Nova Bréscia'), ('Nova Candelária', 'Nova Candelária'), ('Nova Pádua', 'Nova Pádua'), ('Nova Palma', 'Nova Palma'), ('Nova Petrópolis', 'Nova Petrópolis'), ('Nova Prata', 'Nova Prata'), ('Nova Roma Do Sul', 'Nova Roma Do Sul'), ('Nova Santa Rita', 'Nova Santa Rita'), ('Novo Hamburgo', 'Novo Hamburgo'), ('Novo Tiradentes', 'Novo Tiradentes'), ('Novo Xingu', 'Novo Xingu'), ('Novo Barreiro', 'Novo Barreiro'), ('Osório', 'Osório'), ('Paim Filho', 'Paim Filho'), ('Palmeira Das Missões', 'Palmeira Das Missões'), ('Palmitinho', 'Palmitinho'), ('Panambi', 'Panambi'), ('Pantano Grande', 'Pantano Grande'), ('Paraí', 'Paraí'), ('Parobé', 'Parobé'), ('Passo Do Sobrado', 'Passo Do Sobrado'), ('Passo Fundo', 'Passo Fundo'), ('Paverama', 'Paverama'), ('Pelotas', 'Pelotas'), ('Picada Café', 'Picada Café'), ('Pinhal', 'Pinhal'), ('Pinhal Da Serra', 'Pinhal Da Serra'), ('Pinhal Grande', 'Pinhal Grande'), ('Pinheirinho Do Vale', 'Pinheirinho Do Vale'), ('Pinheiro Machado', 'Pinheiro Machado'), ('Piratini', 'Piratini'), ('Planalto', 'Planalto'), ('Poço Das Antas', 'Poço Das Antas'), ('Pontão', 'Pontão'), ('Porto Alegre', 'Porto Alegre'), ('Porto Xavier', 'Porto Xavier'), ('Pouso Novo', 'Pouso Novo'), ('Progresso', 'Progresso'), ('Protásio Alves', 'Protásio Alves'), ('Putinga', 'Putinga'), ('Quaraí', 'Quaraí'), ('Redentora', 'Redentora'), ('Relvado', 'Relvado'), ('Restinga Seca', 'Restinga Seca'), ('Rio Dos Índios', 'Rio Dos Índios'), ('Rio Grande', 'Rio Grande'), ('Rio Pardo', 'Rio Pardo'), ('Roca Sales', 'Roca Sales'), ('Rodeio Bonito', 'Rodeio Bonito'), ('Rolante', 'Rolante'), ('Ronda Alta', 'Ronda Alta'), ('Rosário Do Sul', 'Rosário Do Sul'), ('Sagrada Família', 'Sagrada Família'), ('Salvador Do Sul', 'Salvador Do Sul'), ('Sananduva', 'Sananduva'), ('Santa Cecília Do Sul', 'Santa Cecília Do Sul'), ('Santa Clara Do Sul', 'Santa Clara Do Sul'), ('Santa Cruz Do Sul', 'Santa Cruz Do Sul'), ('Santa Maria', 'Santa Maria'), ('Santana Da Boa Vista', 'Santana Da Boa Vista'), ("Sant'ana Do Livramento", "Sant'ana Do Livramento"), ('Santa Rosa', 'Santa Rosa'), ('Santa Tereza', 'Santa Tereza'), ('Santa Vitória Do Palmar', 'Santa Vitória Do Palmar'), ('Santiago', 'Santiago'), ('Santo Ângelo', 'Santo Ângelo'), ('Santo Antônio Do Palma', 'Santo Antônio Do Palma'), ('Santo Antônio Da Patrulha', 'Santo Antônio Da Patrulha'), ('Santo Antônio Das Missões', 'Santo Antônio Das Missões'), ('Santo Antônio Do Planalto', 'Santo Antônio Do Planalto'), ('Santo Augusto', 'Santo Augusto'), ('Santo Cristo', 'Santo Cristo'), ('Santo Expedito Do Sul', 'Santo Expedito Do Sul'), ('São Borja', 'São Borja'), ('São Domingos Do Sul', 'São Domingos Do Sul'), ('São Francisco De Assis', 'São Francisco De Assis'), ('São Francisco De Paula', 'São Francisco De Paula'), ('São Gabriel', 'São Gabriel'), ('São Jerônimo', 'São Jerônimo'), ('São João Da Urtiga', 'São João Da Urtiga'), ('São Jorge', 'São Jorge'), ('São José Do Herval', 'São José Do Herval'), ('São José Do Inhacorá', 'São José Do Inhacorá'), ('São José Do Norte', 'São José Do Norte'), ('São José Do Ouro', 'São José Do Ouro'), ('São José Dos Ausentes', 'São José Dos Ausentes'), ('São Leopoldo', 'São Leopoldo'), ('São Lourenço Do Sul', 'São Lourenço Do Sul'), ('São Luiz Gonzaga', 'São Luiz Gonzaga'), ('São Marcos', 'São Marcos'), ('São Martinho', 'São Martinho'), ('São Nicolau', 'São Nicolau'), ('São Pedro Da Serra', 'São Pedro Da Serra'), ('São Pedro Do Sul', 'São Pedro Do Sul'), ('São Sebastião Do Caí', 'São Sebastião Do Caí'), ('São Sepé', 'São Sepé'), ('São Vendelino', 'São Vendelino'), ('São Vicente Do Sul', 'São Vicente Do Sul'), ('Sapiranga', 'Sapiranga'), ('Sapucaia Do Sul', 'Sapucaia Do Sul'), ('Sarandi', 'Sarandi'), ('Seberi', 'Seberi'), ('Sede Nova', 'Sede Nova'), ('Serafina Corrêa', 'Serafina Corrêa'), ('Sério', 'Sério'), ('Sertão', 'Sertão'), ('Sertão Santana', 'Sertão Santana'), ('Severiano De Almeida', 'Severiano De Almeida'), ('Sinimbu', 'Sinimbu'), ('Soledade', 'Soledade'), ('Tapejara', 'Tapejara'), ('Tapera', 'Tapera'), ('Tapes', 'Tapes'), ('Taquara', 'Taquara'), ('Taquari', 'Taquari'), ('Tavares', 'Tavares'), ('Tenente Portela', 'Tenente Portela'), ('Terra De Areia', 'Terra De Areia'), ('Teutônia', 'Teutônia'), ('Tio Hugo', 'Tio Hugo'), ('Tiradentes Do Sul', 'Tiradentes Do Sul'), ('Torres', 'Torres'), ('Tramandaí', 'Tramandaí'), ('Três Arroios', 'Três Arroios'), ('Três Cachoeiras', 'Três Cachoeiras'), ('Três Coroas', 'Três Coroas'), ('Três De Maio', 'Três De Maio'), ('Três Palmeiras', 'Três Palmeiras'), ('Três Passos', 'Três Passos'), ('Trindade Do Sul', 'Trindade Do Sul'), ('Triunfo', 'Triunfo'), ('Tucunduva', 'Tucunduva'), ('Tunas', 'Tunas'), ('Tupanci Do Sul', 'Tupanci Do Sul'), ('Tupanciretã', 'Tupanciretã'), ('Tuparendi', 'Tuparendi'), ('União Da Serra', 'União Da Serra'), ('Uruguaiana', 'Uruguaiana'), ('Vacaria', 'Vacaria'), ('Vale Do Sol', 'Vale Do Sol'), ('Vale Real', 'Vale Real'), ('Vanini', 'Vanini'), ('Venâncio Aires', 'Venâncio Aires'), ('Vera Cruz', 'Vera Cruz'), ('Veranópolis', 'Veranópolis'), ('Vespasiano Correa', 'Vespasiano Correa'), ('Viamão', 'Viamão'), ('Vicente Dutra', 'Vicente Dutra'), ('Victor Graeff', 'Victor Graeff'), ('Vila Flores', 'Vila Flores'), ('Vila Maria', 'Vila Maria'), ('Vista Alegre', 'Vista Alegre'), ('Vista Alegre Do Prata', 'Vista Alegre Do Prata'), ('Vitória Das Missões', 'Vitória Das Missões'), ('Westfalia', 'Westfalia'), ('Xangri-lá', 'Xangri-lá'))

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

    color = ColorField("Cor", format="hexa", blank=True)

    def __str__(self):
        return self.name



class Project(models.Model):

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


    name = models.CharField("Nome do Projeto", max_length=50)
    state = models.CharField("Estado", max_length=2, choices=STATE_CHOICES, default=STATE_CHOICES[20][0], editable=False)
    city = models.CharField("Cidade", max_length=60, choices=CITY_CHOICES)

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

    