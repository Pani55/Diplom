from django.urls import path

from medicine.apps import MedicineConfig
from medicine.views import HomeTemplateView, ProceduresListView, ProceduresDetailView

app_name = MedicineConfig.name

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("procedures_list/", ProceduresListView.as_view(), name="procedures_list"),
    path("procedures_detail/<int:pk>/", ProceduresDetailView.as_view(), name="procedures_detail"),
]
