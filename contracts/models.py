from django.db import models
from products.models import Product


def file_path(elem: "Contracts", filename: str) -> str:

    return f"uploads/contracts_{elem.pk}/{filename}"


class Contracts(models.Model):
    class Meta:
        verbose_name_plural = "Contracts"

    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    start_data = models.DateField()
    end_data = models.DateField()
    file = models.FileField(upload_to=file_path)

    def __str__(self):
        return f"Contract(pk={self.pk}, name={self.name!r})"
