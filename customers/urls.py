from django.urls import path
from .views import (CustomersListView, CustomersCreateView,
                    CustomersDeleteView, CustomersDetailView,
                    CustomersUpdateView)

app_name = 'customers'

urlpatterns = [
    path('', CustomersListView.as_view(), name='customers'),
    path('new/', CustomersCreateView.as_view(), name='customers_new'),
    path('<int:pk>/', CustomersDetailView.as_view(), name='customers_detail'),
    path('<int:pk>/delete/', CustomersDeleteView.as_view(), name='customers_delete'),
    path('<int:pk>/edit/', CustomersUpdateView.as_view(), name='customers_edit'),
]
