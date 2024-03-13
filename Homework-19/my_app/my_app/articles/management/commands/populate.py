from django.core.management.base import BaseCommand
from articles.models import Article
from faker import Faker


class Command(BaseCommand):

    help = 'Populate the Article table with 30 records'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(30):
            name = fake.sentence()
            body = fake.paragraph()
            Article.objects.create(name=name, body=body)
        self.stdout.write(self.style.SUCCESS('Successfully populated Article table with 30 records'))