from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import Customer


class CustomersListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Customer
    permission_required = "customers.view_customer"
    template_name = "customers/customers-list.html"
    context_object_name = "customers"


class CustomersCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Customer
    permission_required = "customers.create_customer"
    template_name = "customers/customers-create.html"
    context_object_name = "customers"
    fields = "lead", "contract"
    success_url = reverse_lazy("customers:customers")


class CustomersDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Customer
    permission_required = "customer.delete_customer"
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy("customers:customers")


class CustomersDetailView(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Customer
    permission_required = "customers.view_customer"
    template_name = "customers/customers-detail.html"


class CustomersUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Customer
    permission_required = "customers.change_customer"
    template_name = "customers/customers-edit.html"
    fields = "lead", "contract"

    def get_success_url(self):
        return reverse_lazy("customers:customers_detail", kwargs={"pk": self.object.pk})
