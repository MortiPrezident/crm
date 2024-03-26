from django.core.management import BaseCommand
from django.contrib.auth.models import User
from products.models import Product
from ads.models import Ads


class Command(BaseCommand):
    def handle(self, *args, **options):
        ads_data = [
            {
                'name': 'ads_1',
                'product': Product.objects.get(pk=2),
                'budget': 25000.00,
            },
            {
                'name': 'ads_2',
                'product': Product.objects.get(pk=3),
                'budget': 15000.00,
            },
            {
                'name': 'ads_3',
                'product': Product.objects.get(pk=2),
                'budget': 7000.00,
            },
        ]

        for ads in ads_data:

            name, product,  budget = ads.values()

            ad = Ads.objects.create(
                name=name, product=product, budget=budget)


