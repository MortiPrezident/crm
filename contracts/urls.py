from django.urls import path
from .views import (
    ContractsListView,
    ContractsCreateView,
    ContractsDeleteView,
    ContractsDetailView,
    ContractsUpdateView,
)


app_name = "contracts"

urlpatterns = [
    path("", ContractsListView.as_view(), name="contracts"),
    path("new/", ContractsCreateView.as_view(), name="contracts_new"),
    path("<int:pk>/", ContractsDetailView.as_view(), name="contracts_detail"),
    path("<int:pk>/delete/", ContractsDeleteView.as_view(), name="contracts_delete"),
    path("<int:pk>/edit/", ContractsUpdateView.as_view(), name="contracts_edit"),
]
