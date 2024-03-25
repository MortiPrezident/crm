from django.core.management import BaseCommand
from django.contrib.auth.models import User
from products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products_data = [
            {
                'name': 'product_1',
                'description': 'cool product',
                'price': 2500.00,
            },
            {
                'name': 'product_2',
                'description': 'cool product 2',
                'price': 3500.00,
            },
            {
                'name': 'product_3',
                'description': 'cool product 3',
                'price': 5500.00,
            },
        ]

        for product in products_data:
            name, description,  price = product.values()

            Product.objects.create(
                name=name, description=description, price=price)


