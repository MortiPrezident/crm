from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Ads
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class AdsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Ads
    template_name = 'ads/ads-list.html'
    permission_required = 'ads.view_ads'
    context_object_name = 'ads'


class AdsDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Ads
    template_name = 'ads/ads-detail.html'
    permission_required = 'ads.view_ads'


class AdsDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Ads
    template_name = 'ads/ads-delete.html'
    permission_required = 'ads.delete_ads'
    success_url = reverse_lazy('ads:ads')


class AdsCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Ads
    template_name = 'ads/ads-create.html'
    permission_required = 'ads.create_ads'
    success_url = reverse_lazy('ads:ads')
    fields = 'name', 'budget', 'product',


class AdsStatisticListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Ads
    template_name = 'ads/ads-statistic.html'
    permission_required = 'ads.view_ads'
    context_object_name = 'ads'


class AdsUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Ads
    permission_required = 'ads.change_ads'
    template_name = 'ads/ads-edit.html'
    fields = 'name', 'budget', 'product', 'leads_count', 'customers_count', 'profit'

    def get_success_url(self):
        return reverse_lazy('ads:ads_detail', kwargs={'pk': self.object.pk})
