from django.shortcuts import render
from customers.models import Customer
from products.models import Product
from ads.models import Ads
from leads.models import Leads


def home_view(request):
    customers_count = Customer.objects.all().count()
    products_count = Product.objects.all().count()
    advertisements_count = Ads.objects.all().count()
    leads_count = Leads.objects.all().count()

    context = {
        "customers_count": customers_count,
        "products_count": products_count,
        "advertisements_count": advertisements_count,
        "leads_count": leads_count,
    }

    return render(request, "home/index.html", context=context)
