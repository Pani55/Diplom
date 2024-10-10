from django.contrib import admin

from medicine.models import Procedures, Doctors, Appointment, Feedback


@admin.register(Procedures)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ("title",  "description", "price")
    search_fields = ("title",)


@admin.register(Doctors)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "specialization",)
    list_filter = ("specialization",)
    search_fields = ("last_name",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("doctor", "patient", "appointment_datetime", "procedure")
    list_filter = ("doctor", "patient", "appointment_datetime", "procedure")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("user", "text")
    search_fields = ("user",)
