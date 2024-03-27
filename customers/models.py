from django.db import models
from leads.models import Leads
from contracts.models import Contracts


class Customer(models.Model):
    lead = models.OneToOneField(Leads, on_delete=models.CASCADE)
    contract = models.OneToOneField(Contracts, on_delete=models.CASCADE)
