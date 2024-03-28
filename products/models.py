from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"Product(pk={self.pk}, name={self.name!r})"
