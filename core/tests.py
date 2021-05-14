from django.test import TestCase
from .models import Data


class DataTestCase(TestCase):
    def setUp(self):
        Data.objects.create(year=2008, country="Nepal", product="Oxygen", sale=52147)
        Data.objects.create(year=2009, country="USA", product="Plant", sale=2147)
        Data.objects.create(year=2008, country="USA", product="Oxygen", sale=365552147)
        Data.objects.create(year=2007, country="Russia", product="Plant", sale=44452147)
        Data.objects.create(year=2009, country="Nepal", product="Plant", sale=3652147)

    def test_check_Database(self):
        data = Data.objects.get(year=2008, country="Nepal")
        data1 = Data.objects.filter(sale=2147).first()

        self.assertEqual(data.__str__(), "Oxygen")
        self.assertEquals(data1.__str__(), "Plant")
