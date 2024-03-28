from django.urls import path
from .views import LeadsListView, LeadsCreateView, LeadsDeleteView, LeadsDetailView, LeadsUpdateView

app_name = "leads"


urlpatterns = [
    path("", LeadsListView.as_view(), name="leads"),
    path("new/", LeadsCreateView.as_view(), name="leads_new"),
    path("<int:pk>/", LeadsDetailView.as_view(), name="leads_detail"),
    path("<int:pk>/edit", LeadsUpdateView.as_view(), name="leads_edit"),
    path("<int:pk>/delete/", LeadsDeleteView.as_view(), name="leads_delete"),
]
