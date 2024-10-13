from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from medicine.forms import FeedbackForm
from medicine.models import Procedures, Feedback, Doctors, Appointment


class HomeTemplateView(TemplateView):
    """ This view is designed to display the main page """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['procedures_list'] = Procedures.objects.all()
        return context


class ProceduresListView(ListView):
    """ This view is designed to display a list of procedures. """
    model = Procedures


class ProceduresDetailView(DetailView):
    """ This view is designed to display a detailed procedure """
    model = Procedures


class FeedbackCreateView(CreateView):
    """ This view is designed to create a new Feedback object """
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback_form.html'
    success_url = '/'

    def form_valid(self, form):
        """ With this method, the feedback object is automatically assigned an owner user """
        form.instance.user = self.request.user
        return super().form_valid(form)


class DoctorsListView(ListView):
    """ This view is designed to display a list of doctors. """
    model = Doctors


class ContactInfoView(TemplateView):
    """ This view is designed to display contact information page. """
    template_name = "medicine/contact_info.html"


class AppointmentListView(ListView):
    """ This view is designed to display a list of appointments. """
    model = Appointment

    def get_queryset(self):
        """ Get appointments that are owned by a user """
        return Appointment.objects.filter(patient=self.request.user)


class AppointmentCreateView(CreateView):
    """ This view is designed to create a new appointment object. """
    model = Appointment
    fields = ['doctor', 'procedure', 'appointment_datetime']
    success_url = reverse_lazy('medicine:appointment_list')

    def form_valid(self, form):
        """ With this method, the appointment object is automatically assigned an owner user(patient) """
        form.instance.patient = self.request.user
        return super().form_valid(form)
