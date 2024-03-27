from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import Leads


class LeadsListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Leads
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'
    permission_required = 'leads.view_leads'


class LeadsCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Leads
    template_name = 'leads/leads-create.html'
    permission_required = 'leads.create_leads'
    fields = 'first_name', 'last_name', 'email', 'phone', 'ad'
    success_url = reverse_lazy('leads:leads')


class LeadsDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Leads
    template_name = 'leads/leads-delete.html'
    permission_required = 'leads.delete_leads'
    success_url = reverse_lazy('leads:leads')


class LeadsDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Leads
    template_name = 'leads/leads-detail.html'
    permission_required = 'leads.view_leads'
    fields = 'first_name', 'last_name', 'email', 'phone', 'ad'


class LeadsUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Leads
    template_name = 'leads/leads-edit.html'
    permission_required = 'leads.change_leads'
    fields = 'first_name', 'last_name', 'email', 'phone', 'ad'

    def get_success_url(self):
        return reverse_lazy('leads:leads_detail', kwargs={'pk': self.object.pk})

