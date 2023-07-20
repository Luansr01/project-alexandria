from django.core.management.base import BaseCommand, CommandError
from alexandria_site.models import Objective

ODS = (
    "Erradicação da Pobreza",
    "Fome Zero",
    "Boa Saúde e Bem-Estar",
    "Educação de Qualidade",
    "Igualdade de Gênero",
    "Água Potável e Saneamento",
    "Energia Acessível e Limpa",
    "Trabalho Decente e Crescimento Econômico",
    "Indústria, Inovação e Infraestrutura",
    "Reduzir as Desigualdades",
    "Cidades e Comunidades Sustentáveis",
    "Consumo e Produção Responsáveis",
    "Ação Climática",
    "Vida na Água",
    "Vida Terrestre",
    "Paz, Justiça e Instituições Sólidas",
    "Parcerias para os Objetivos",
)

class Command(BaseCommand):
    help = "Populates the db with the ONU objectives"

    def handle(self, *args, **options):
        for objective in ODS:
            Objective.objects.create(name=objective)
            self.stdout.write(self.style.SUCCESS(objective + "Added successfully!"))