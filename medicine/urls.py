from django.urls import path

from medicine.apps import MedicineConfig
from medicine.views import (HomeTemplateView, ProceduresListView,
                            ProceduresDetailView, FeedbackCreateView,
                            DoctorsListView, ContactInfoView)

app_name = MedicineConfig.name

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("procedures_list/", ProceduresListView.as_view(), name="procedures_list"),
    path("procedures_detail/<int:pk>/", ProceduresDetailView.as_view(), name="procedures_detail"),
    path("feedback_create/", FeedbackCreateView.as_view(), name="feedback_create"),
    path("doctors_list/", DoctorsListView.as_view(), name="doctors_list"),
    path("contact_info/", ContactInfoView.as_view(), name="contact_info"),
]
