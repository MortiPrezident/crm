from django.db import models
from products.models import Product


class Ads(models.Model):

    class Meta:
        verbose_name_plural = "ads"

    name = models.CharField(max_length=40)
    budget = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    leads_count = models.IntegerField(default=0)
    customers_count = models.IntegerField(default=0)
    profit = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Ads(pk={self.pk}, name={self.name!r})'
