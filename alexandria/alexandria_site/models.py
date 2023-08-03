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

CITY_CHOICES =  (
    ('ACEGUÁ', 'Aceguá'), ('ÁGUA SANTA', 'Água Santa'), ('AGUDO', 'Agudo'),
    ('AJURICABA', 'Ajuricaba'), ('ALECRIM', 'Alecrim'), ('ALEGRETE', 'Alegrete'),
    ('ALMIRANTE TAMANDARÉ DO SUL', 'Almirante Tamandaré Do Sul'), ('ALPESTRE', 'Alpestre'),
    ('ALTO ALEGRE', 'Alto Alegre'), ('ALVORADA', 'Alvorada'), ('AMETISTA DO SUL', 'Ametista Do Sul'),
    ('ANDRÉ DA ROCHA', 'André Da Rocha'), ('ANTA GORDA', 'Anta Gorda'), ('ANTÔNIO PRADO', 'Antônio Prado'),
    ('ARATIBA', 'Aratiba'), ('ARROIO DO MEIO', 'Arroio Do Meio'), ('ARROIO DO SAL', 'Arroio Do Sal'), 
    ('ARROIO DO TIGRE', 'Arroio Do Tigre'), ('ARROIO GRANDE', 'Arroio Grande'), ('ARVOREZINHA', 'Arvorezinha'),
    ('AUGUSTO PESTANA', 'Augusto Pestana'), ('BAGÉ', 'Bagé'), ('BALNEÁRIO PINHAL', 'Balneário Pinhal'),
    ('BARÃO DE COTEGIPE', 'Barão De Cotegipe'), ('BARÃO DO TRIUNFO', 'Barão Do Triunfo'), ('BARRACÃO', 'Barracão'),
    ('BARRA DO QUARAÍ', 'Barra Do Quaraí'), ('BARRA DO RIBEIRO', 'Barra Do Ribeiro'), ('BARRA FUNDA', 'Barra Funda'), 
    ('BARROS CASSAL', 'Barros Cassal'), ('BENTO GONÇALVES', 'Bento Gonçalves'), ('BOA VISTA DAS MISSÕES', 'Boa Vista Das Missões'),
    ('BOA VISTA DO BURICÁ', 'Boa Vista Do Buricá'), ('BOA VISTA DO CADEADO', 'Boa Vista Do Cadeado'), 
    ('BOA VISTA DO SUL', 'Boa Vista Do Sul'), ('BOM JESUS', 'Bom Jesus'), ('BOM PRINCÍPIO', 'Bom Princípio'),
    ('BOM RETIRO DO SUL', 'Bom Retiro Do Sul'), ('BOQUEIRÃO DO LEÃO', 'Boqueirão Do Leão'), ('BRAGA', 'Braga'),
    ('BROCHIER', 'Brochier'), ('BUTIÁ', 'Butiá'), ('CAÇAPAVA DO SUL', 'Caçapava Do Sul'), ('CACEQUI', 'Cacequi'),
    ('CACHOEIRA DO SUL', 'Cachoeira Do Sul'), ('CACHOEIRINHA', 'Cachoeirinha'), ('CACIQUE DOBLE', 'Cacique Doble'),
    ('CAIBATÉ', 'Caibaté'), ('CAIÇARA', 'Caiçara'), ('CAMAQUÃ', 'Camaquã'), ('CAMARGO', 'Camargo'),
    ('CAMBARÁ DO SUL', 'Cambará Do Sul'), ('CAMPESTRE DA SERRA', 'Campestre Da Serra'),
    ('CAMPINAS DO SUL', 'Campinas Do Sul'), ('CAMPO BOM', 'Campo Bom'), ('CAMPOS BORGES', 'Campos Borges'), 
    ('CANDELÁRIA', 'Candelária'), ('CÂNDIDO GODÓI', 'Cândido Godói'), ('CANDIOTA', 'Candiota'),
    ('CANELA', 'Canela'), ('CANGUÇU', 'Canguçu'), ('CANOAS', 'Canoas'), ('CAPÃO BONITO DO SUL', 'Capão Bonito Do Sul'),
    ('CAPÃO DA CANOA', 'Capão Da Canoa'), ('CAPÃO DO LEÃO', 'Capão Do Leão'), ('CARAZINHO', 'Carazinho'),
    ('CARLOS BARBOSA', 'Carlos Barbosa'), ('CASCA', 'Casca'), ('CASEIROS', 'Caseiros'),
    ('CAXIAS DO SUL', 'Caxias Do Sul'), ('CERRO GRANDE', 'Cerro Grande'), ('CERRO LARGO', 'Cerro Largo'),
    ('CHAPADA', 'Chapada'), ('CHARQUEADAS', 'Charqueadas'), ('CHARRUA', 'Charrua'), ('CHIAPETTA', 'Chiapetta'), 
    ('CIRÍACO', 'Ciríaco'), ('COLORADO', 'Colorado'), ('CONDOR', 'Condor'), ('CONSTANTINA', 'Constantina'),
    ('COQUEIROS DO SUL', 'Coqueiros Do Sul'), ('CORONEL BARROS', 'Coronel Barros'), ('CORONEL BICACO', 'Coronel Bicaco'),
    ('CORONEL PILAR', 'Coronel Pilar'), ('COTIPORÃ', 'Cotiporã'), ('CRISSIUMAL', 'Crissiumal'), ('CRISTAL', 'Cristal'),
    ('CRISTAL DO SUL', 'Cristal Do Sul'), ('CRUZ ALTA', 'Cruz Alta'), ('CRUZALTENSE', 'Cruzaltense'),
    ('CRUZEIRO DO SUL', 'Cruzeiro Do Sul'), ('DAVID CANABARRO', 'David Canabarro'), ('DERRUBADAS', 'Derrubadas'),
    ('DOIS IRMÃOS', 'Dois Irmãos'), ('DOM FELICIANO', 'Dom Feliciano'), ('DOM PEDRO DE ALCÂNTARA', 'Dom Pedro De Alcântara'),
    ('DOM PEDRITO', 'Dom Pedrito'), ('DONA FRANCISCA', 'Dona Francisca'), ('ELDORADO DO SUL', 'Eldorado Do Sul'), 
    ('ENCANTADO', 'Encantado'), ('ENCRUZILHADA DO SUL', 'Encruzilhada Do Sul'), ('ENGENHO VELHO', 'Engenho Velho'), 
    ('ENTRE-IJUÍS', 'Entre-ijuís'), ('ENTRE RIOS DO SUL', 'Entre Rios Do Sul'), ('ERECHIM', 'Erechim'),
    ('ERNESTINA', 'Ernestina'), ('ERVAL GRANDE', 'Erval Grande'), ('ERVAL SECO', 'Erval Seco'), ('ESMERALDA', 'Esmeralda'),
    ('ESPUMOSO', 'Espumoso'), ('ESTÂNCIA VELHA', 'Estância Velha'), ('ESTEIO', 'Esteio'), ('ESTRELA', 'Estrela'),
    ('FAGUNDES VARELA', 'Fagundes Varela'), ('FARROUPILHA', 'Farroupilha'), ('FAXINAL DO SOTURNO', 'Faxinal Do Soturno'),
    ('FAZENDA VILANOVA', 'Fazenda Vilanova'), ('FELIZ', 'Feliz'), ('FLORES DA CUNHA', 'Flores Da Cunha'),
    ('FONTOURA XAVIER', 'Fontoura Xavier'), ('FORQUETINHA', 'Forquetinha'), ('FORTALEZA DOS VALOS', 'Fortaleza Dos Valos'), 
    ('FREDERICO WESTPHALEN', 'Frederico Westphalen'), ('GARIBALDI', 'Garibaldi'), ('GENERAL CÂMARA', 'General Câmara'),
    ('GENTIL', 'Gentil'), ('GETÚLIO VARGAS', 'Getúlio Vargas'), ('GIRUÁ', 'Giruá'), ('GRAMADO', 'Gramado'),
    ('GRAMADO XAVIER', 'Gramado Xavier'), ('GRAVATAÍ', 'Gravataí'), ('GUABIJU', 'Guabiju'), ('GUAÍBA', 'Guaíba'), 
    ('GUAPORÉ', 'Guaporé'), ('GUARANI DAS MISSÕES', 'Guarani Das Missões'), ('HORIZONTINA', 'Horizontina'), 
    ('HUMAITÁ', 'Humaitá'), ('IBIAÇÁ', 'Ibiaçá'), ('IBIRAIARAS', 'Ibiraiaras'), ('IBIRAPUITÃ', 'Ibirapuitã'),
    ('IBIRUBÁ', 'Ibirubá'), ('IGREJINHA', 'Igrejinha'), ('IJUÍ', 'Ijuí'), ('ILÓPOLIS', 'Ilópolis'), ('IMBÉ', 'Imbé'),
    ('IMIGRANTE', 'Imigrante'), ('INDEPENDÊNCIA', 'Independência'), ('IPÊ', 'Ipê'), ('IRAÍ', 'Iraí'), 
    ('ITAPUCA', 'Itapuca'), ('ITAQUI', 'Itaqui'), ('ITATIBA DO SUL', 'Itatiba Do Sul'), ('IVOTI', 'Ivoti'), 
    ('JABOTICABA', 'Jaboticaba'), ('JAGUARÃO', 'Jaguarão'), ('JAGUARI', 'Jaguari'), ('JAQUIRANA', 'Jaquirana'), 
    ('JÓIA', 'Jóia'), ('JÚLIO DE CASTILHOS', 'Júlio De Castilhos'), ('LAGOÃO', 'Lagoão'), 
    ('LAGOA DOS TRÊS CANTOS', 'Lagoa Dos Três Cantos'), ('LAGOA VERMELHA', 'Lagoa Vermelha'), ('LAJEADO', 'Lajeado'),
    ('LAVRAS DO SUL', 'Lavras Do Sul'), ('LIBERATO SALZANO', 'Liberato Salzano'), ('LINHA NOVA', 'Linha Nova'),
    ('MACHADINHO', 'Machadinho'), ('MANOEL VIANA', 'Manoel Viana'), ('MARATÁ', 'Maratá'), ('MARAU', 'Marau'), 
    ('MARCELINO RAMOS', 'Marcelino Ramos'), ('MARQUES DE SOUZA', 'Marques De Souza'), ('MATO CASTELHANO', 'Mato Castelhano'),
    ('MATO LEITÃO', 'Mato Leitão'), ('MAXIMILIANO DE ALMEIDA', 'Maximiliano De Almeida'), ('MINAS DO LEÃO', 'Minas Do Leão'),
    ('MIRAGUAÍ', 'Miraguaí'), ('MONTAURI', 'Montauri'), ('MONTE ALEGRE DOS CAMPOS', 'Monte Alegre Dos Campos'), 
    ('MONTE BELO DO SUL', 'Monte Belo Do Sul'), ('MONTENEGRO', 'Montenegro'), ('MORMAÇO', 'Mormaço'), ('MUÇUM', 'Muçum'), 
    ('MUITOS CAPÕES', 'Muitos Capões'), ('MULITERNO', 'Muliterno'), ('NICOLAU VERGUEIRO', 'Nicolau Vergueiro'),
    ('NONOAI', 'Nonoai'), ('NOVA ALVORADA', 'Nova Alvorada'), ('NOVA ARAÇÁ', 'Nova Araçá'), ('NOVA BASSANO', 'Nova Bassano'),
    ('NOVA BOA VISTA', 'Nova Boa Vista'), ('NOVA BRÉSCIA', 'Nova Bréscia'), ('NOVA CANDELÁRIA', 'Nova Candelária'),
    ('NOVA PÁDUA', 'Nova Pádua'), ('NOVA PALMA', 'Nova Palma'), ('NOVA PETRÓPOLIS', 'Nova Petrópolis'),
    ('NOVA PRATA', 'Nova Prata'), ('NOVA ROMA DO SUL', 'Nova Roma Do Sul'), ('NOVA SANTA RITA', 'Nova Santa Rita'), 
    ('NOVO HAMBURGO', 'Novo Hamburgo'), ('NOVO TIRADENTES', 'Novo Tiradentes'), ('NOVO XINGU', 'Novo Xingu'),
    ('NOVO BARREIRO', 'Novo Barreiro'), ('OSÓRIO', 'Osório'), ('PAIM FILHO', 'Paim Filho'), 
    ('PALMEIRA DAS MISSÕES', 'Palmeira Das Missões'), ('PALMITINHO', 'Palmitinho'), ('PANAMBI', 'Panambi'),
    ('PANTANO GRANDE', 'Pantano Grande'), ('PARAÍ', 'Paraí'), ('PAROBÉ', 'Parobé'),
    ('PASSO DO SOBRADO', 'Passo Do Sobrado'), ('PASSO FUNDO', 'Passo Fundo'), ('PAVERAMA', 'Paverama'), ('PELOTAS', 'Pelotas'),
    ('PICADA CAFÉ', 'Picada Café'), ('PINHAL', 'Pinhal'), ('PINHAL DA SERRA', 'Pinhal Da Serra'), ('PINHAL GRANDE', 'Pinhal Grande'),
    ('PINHEIRINHO DO VALE', 'Pinheirinho Do Vale'), ('PINHEIRO MACHADO', 'Pinheiro Machado'), ('PIRATINI', 'Piratini'),
    ('PLANALTO', 'Planalto'), ('POÇO DAS ANTAS', 'Poço Das Antas'), ('PONTÃO', 'Pontão'), ('PORTO ALEGRE', 'Porto Alegre'),
    ('PORTO XAVIER', 'Porto Xavier'), ('POUSO NOVO', 'Pouso Novo'), ('PROGRESSO', 'Progresso'), ('PROTÁSIO ALVES', 'Protásio Alves'),
    ('PUTINGA', 'Putinga'), ('QUARAÍ', 'Quaraí'), ('REDENTORA', 'Redentora'), ('RELVADO', 'Relvado'),
    ('RESTINGA SECA', 'Restinga Seca'), ('RIO DOS ÍNDIOS', 'Rio Dos Índios'), ('RIO GRANDE', 'Rio Grande'), 
    ('RIO PARDO', 'Rio Pardo'), ('ROCA SALES', 'Roca Sales'), ('RODEIO BONITO', 'Rodeio Bonito'),
    ('ROLANTE', 'Rolante'), ('RONDA ALTA', 'Ronda Alta'), ('ROSÁRIO DO SUL', 'Rosário Do Sul'),
    ('SAGRADA FAMÍLIA', 'Sagrada Família'), ('SALVADOR DO SUL', 'Salvador Do Sul'), ('SANANDUVA', 'Sananduva'),
    ('SANTA CECÍLIA DO SUL', 'Santa Cecília Do Sul'), ('SANTA CLARA DO SUL', 'Santa Clara Do Sul'),
    ('SANTA CRUZ DO SUL', 'Santa Cruz Do Sul'), ('SANTA MARIA', 'Santa Maria'),
    ('SANTANA DA BOA VISTA', 'Santana Da Boa Vista'), ("SANT'ANA DO LIVRAMENTO", "Sant'ana Do Livramento"),
    ('SANTA ROSA', 'Santa Rosa'), ('SANTA TEREZA', 'Santa Tereza'), 
    ('SANTA VITÓRIA DO PALMAR', 'Santa Vitória Do Palmar'), ('SANTIAGO', 'Santiago'),
    ('SANTO ÂNGELO', 'Santo Ângelo'), ('SANTO ANTÔNIO DO PALMA', 'Santo Antônio Do Palma'),
    ('SANTO ANTÔNIO DA PATRULHA', 'Santo Antônio Da Patrulha'), ('SANTO ANTÔNIO DAS MISSÕES', 'Santo Antônio Das Missões'),
    ('SANTO ANTÔNIO DO PLANALTO', 'Santo Antônio Do Planalto'), ('SANTO AUGUSTO', 'Santo Augusto'),
    ('SANTO CRISTO', 'Santo Cristo'), ('SANTO EXPEDITO DO SUL', 'Santo Expedito Do Sul'), ('SÃO BORJA', 'São Borja'),
    ('SÃO DOMINGOS DO SUL', 'São Domingos Do Sul'), ('SÃO FRANCISCO DE ASSIS', 'São Francisco De Assis'), 
    ('SÃO FRANCISCO DE PAULA', 'São Francisco De Paula'), ('SÃO GABRIEL', 'São Gabriel'), 
    ('SÃO JERÔNIMO', 'São Jerônimo'), ('SÃO JOÃO DA URTIGA', 'São João Da Urtiga'),
    ('SÃO JORGE', 'São Jorge'), ('SÃO JOSÉ DO HERVAL', 'São José Do Herval'),
    ('SÃO JOSÉ DO INHACORÁ', 'São José Do Inhacorá'), ('SÃO JOSÉ DO NORTE', 'São José Do Norte'),
    ('SÃO JOSÉ DO OURO', 'São José Do Ouro'), ('SÃO JOSÉ DOS AUSENTES', 'São José Dos Ausentes'),
    ('SÃO LEOPOLDO', 'São Leopoldo'), ('SÃO LOURENÇO DO SUL', 'São Lourenço Do Sul'), 
    ('SÃO LUIZ GONZAGA', 'São Luiz Gonzaga'), ('SÃO MARCOS', 'São Marcos'), ('SÃO MARTINHO', 'São Martinho'), 
    ('SÃO NICOLAU', 'São Nicolau'), ('SÃO PEDRO DA SERRA', 'São Pedro Da Serra'),
    ('SÃO PEDRO DO SUL', 'São Pedro Do Sul'), ('SÃO SEBASTIÃO DO CAÍ', 'São Sebastião Do Caí'), ('SÃO SEPÉ', 'São Sepé'),
    ('SÃO VENDELINO', 'São Vendelino'), ('SÃO VICENTE DO SUL', 'São Vicente Do Sul'), ('SAPIRANGA', 'Sapiranga'), 
    ('SAPUCAIA DO SUL', 'Sapucaia Do Sul'), ('SARANDI', 'Sarandi'), ('SEBERI', 'Seberi'), ('SEDE NOVA', 'Sede Nova'),
    ('SERAFINA CORRÊA', 'Serafina Corrêa'), ('SÉRIO', 'Sério'), ('SERTÃO', 'Sertão'), ('SERTÃO SANTANA', 'Sertão Santana'),
    ('SEVERIANO DE ALMEIDA', 'Severiano De Almeida'), ('SINIMBU', 'Sinimbu'), ('SOLEDADE', 'Soledade'), ('TAPEJARA', 'Tapejara'), 
    ('TAPERA', 'Tapera'), ('TAPES', 'Tapes'), ('TAQUARA', 'Taquara'), ('TAQUARI', 'Taquari'), ('TAVARES', 'Tavares'), ('TENENTE PORTELA', 'Tenente Portela'),
    ('TERRA DE AREIA', 'Terra De Areia'), ('TEUTÔNIA', 'Teutônia'), ('TIO HUGO', 'Tio Hugo'), ('TIRADENTES DO SUL', 'Tiradentes Do Sul'),
    ('TORRES', 'Torres'), ('TRAMANDAÍ', 'Tramandaí'), ('TRÊS ARROIOS', 'Três Arroios'), ('TRÊS CACHOEIRAS', 'Três Cachoeiras'),
    ('TRÊS COROAS', 'Três Coroas'), ('TRÊS DE MAIO', 'Três De Maio'), ('TRÊS PALMEIRAS', 'Três Palmeiras'), ('TRÊS PASSOS', 'Três Passos'),
    ('TRINDADE DO SUL', 'Trindade Do Sul'), ('TRIUNFO', 'Triunfo'), ('TUCUNDUVA', 'Tucunduva'), ('TUNAS', 'Tunas'), ('TUPANCI DO SUL', 'Tupanci Do Sul'),
    ('TUPANCIRETÃ', 'Tupanciretã'), ('TUPARENDI', 'Tuparendi'), ('UNIÃO DA SERRA', 'União Da Serra'), ('URUGUAIANA', 'Uruguaiana'), ('VACARIA', 'Vacaria'),
    ('VALE DO SOL', 'Vale Do Sol'), ('VALE REAL', 'Vale Real'), ('VANINI', 'Vanini'), ('VENÂNCIO AIRES', 'Venâncio Aires'),
    ('VERA CRUZ', 'Vera Cruz'), ('VERANÓPOLIS', 'Veranópolis'), ('VESPASIANO CORREA', 'Vespasiano Correa'), ('VIAMÃO', 'Viamão'),
    ('VICENTE DUTRA', 'Vicente Dutra'), ('VICTOR GRAEFF', 'Victor Graeff'), ('VILA FLORES', 'Vila Flores'), ('VILA MARIA', 'Vila Maria'),
    ('VISTA ALEGRE', 'Vista Alegre'), ('VISTA ALEGRE DO PRATA', 'Vista Alegre Do Prata'), ('VITÓRIA DAS MISSÕES', 'Vitória Das Missões'),
    ('WESTFALIA', 'Westfalia'), ('XANGRI-LÁ', 'Xangri-lá')
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

    