# Generated by Django 5.0.3 on 2024-03-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
