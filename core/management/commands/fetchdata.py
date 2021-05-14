from django.core.management.base import BaseCommand, CommandError
from core.models import Data
import requests as req


class Command(BaseCommand):
    help = "Update DB"

    def handle(self, *args, **options):
        if not Data.objects.exists():
            url = "https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json"
            res = req.get(url).json()

            try:
                for i in res:
                    info = Data()
                    info.year = i["year"]
                    info.sale = i["sale"]
                    info.product = i["petroleum_product"]
                    info.country = i["country"]
                    info.save()
            except Exception as e:
                raise CommandError(e)
            self.stdout.write(self.style.SUCCESS("Successfully fetched data"))

        else:
            pass
