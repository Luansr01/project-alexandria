from django.core.management.base import BaseCommand, CommandError
from alexandria_site.models import Objective

ODS = (
    ("Erradicação da Pobreza", "#E5243B"),
    ("Fome Zero", "#DDA83AFF"),
    ("Boa Saúde e Bem-Estar", "#4c9c3c"),
    ("Educação de Qualidade", "#C5192D"),
    ("Igualdade de Gênero", "#FF3A21"),
    ("Água Potável e Saneamento", "#26BDE2"),
    ("Energia Acessível e Limpa", "#FCC30B"),
    ("Trabalho Decente e Crescimento Econômico", "#A21942"),
    ("Indústria, Inovação e Infraestrutura", "#FD6925"),
    ("Reduzir as Desigualdades", "#DD1367"),
    ("Cidades e Comunidades Sustentáveis", "#FD9D24"),
    ("Consumo e Produção Responsáveis", "#BF8B2E"),
    ("Ação Climática", "#3F7E44"),
    ("Vida na Água", "#0A97D9"),
    ("Vida Terrestre", "#56C02B"),
    ("Paz, Justiça e Instituições Sólidas", "#00689D"),
    ("Parcerias para os Objetivos", "#19486A"),
)

class Command(BaseCommand):
    help = "Populates the db with the ONU objectives"

    def handle(self, *args, **options):
        for objective in ODS:
            if(not (objective[0] in [x.name for x in Objective.objects.all()])):
                Objective.objects.create(name=objective[0], color=objective[1])
                self.stdout.write(self.style.SUCCESS(objective[0] + " Added successfully!"))
            else:
                self.stdout.write("Objective already exists.")
