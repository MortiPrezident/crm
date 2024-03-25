from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Product


class ProductListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'products.view_product'
    template_name = 'products/products-list.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class ProductCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'products.add_product'
    template_name = 'products/products-create.html'
    model = Product
    fields = 'name', 'description', 'price'
    success_url = reverse_lazy('products:products')


class ProductDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product
    permission_required = 'products.delete_product'
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products')


class ProductDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Product
    permission_required = 'products.view_product'
    template_name = 'products/products-detail.html'


class ProductUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Product
    permission_required = 'products.change_product'
    template_name = 'products/products-edit.html'
    fields = 'name', 'description', 'price'

    def get_success_url(self):
        return reverse_lazy('products:detail_product', kwargs={'pk': self.object.pk})