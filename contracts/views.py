from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import Contracts
from .forms import ContractForm


class ContractsListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Contracts
    template_name = "contracts/contracts-list.html"
    permission_required = "contracts.view_contracts"
    context_object_name = "contracts"


class ContractsCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = "contracts/contracts-create.html"
    permission_required = "contracts.create_contracts"
    form_class = ContractForm
    success_url = reverse_lazy("contracts:contracts")


class ContractsDeleteView(DeleteView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Contracts
    template_name = "contracts/contracts-delete.html"
    permission_required = "contracts.delete_contracts"
    success_url = reverse_lazy("contracts:contracts")


class ContractsDetailView(DetailView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Contracts
    template_name = "contracts/contracts-detail.html"
    permission_required = "contracts.view_contracts"


class ContractsUpdateView(UpdateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Contracts
    template_name = "contracts/contracts-edit.html"
    permission_required = "contracts.change_contracts"
    form_class = ContractForm

    def get_success_url(self):
        return reverse("contracts:contracts_detail", kwargs={"pk": self.object.pk})
