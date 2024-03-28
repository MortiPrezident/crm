from django.core.management import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = [
            {
                "name": "oleg",
                "email": "2@mail.ru",
                "password": "oleg",
                "position": "Оператор",
            },
            {
                "name": "slava",
                "email": "3@mail.ru",
                "password": "slava",
                "position": "Маркетолог",
            },
            {
                "name": "egor",
                "email": "4@mail.ru",
                "password": "egor",
                "position": "Менеджер",
            },
        ]

        for user in user_data:
            name, email, password, position = user.values()

            Profile.objects.create(
                user=User.objects.create_user(
                    username=name, email=email, password=password
                ),
                position=position,
            )
