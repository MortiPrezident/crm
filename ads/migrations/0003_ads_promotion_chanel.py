# Generated by Django 5.0.3 on 2024-03-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ads_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='promotion_chanel',
            field=models.CharField(default='internet', max_length=40),
        ),
    ]
