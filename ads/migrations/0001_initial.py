# Generated by Django 5.0.3 on 2024-03-26 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('budget', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('leads_count', models.IntegerField(default=0)),
                ('customers_count', models.IntegerField(default=0)),
                ('profit', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
