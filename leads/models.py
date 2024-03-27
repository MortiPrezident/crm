from django.db import models
from ads.models import Ads


class Leads(models.Model):

    class Meta:
        verbose_name_plural = "Leads"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=11)
    ad = models.ForeignKey(Ads, on_delete=models.PROTECT)

    def __str__(self):
        return f'Leads(pk={self.pk}, name={self.first_name!r}{self.last_name})'
