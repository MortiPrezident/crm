from django.urls import path
from .views import (
    AdsListView,
    AdsDetailView,
    AdsDeleteView,
    AdsUpdateView,
    AdsCreateView,
    AdsStatisticListView,
)

app_name = "ads"

urlpatterns = [
    path("", AdsListView.as_view(), name="ads"),
    path("new/", AdsCreateView.as_view(), name="ads_new"),
    path("statistic/", AdsStatisticListView.as_view(), name="ads_statistic"),
    path("<int:pk>/", AdsDetailView.as_view(), name="ads_detail"),
    path("<int:pk>/edit", AdsUpdateView.as_view(), name="ads_edit"),
    path("<int:pk>/delete", AdsDeleteView.as_view(), name="ads_delete"),
]
