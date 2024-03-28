from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductUpdateView,
)

app_name = "products"


urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path(
        "new/",
        ProductCreateView.as_view(),
        name="new_product",
    ),
    path("<int:pk>/", ProductDetailView.as_view(), name="detail_product"),
    path("<int:pk>/edit", ProductUpdateView.as_view(), name="edit_product"),
    path("<int:pk>/delete", ProductDeleteView.as_view(), name="delete_product"),
]
