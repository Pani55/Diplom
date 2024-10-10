from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from medicine.forms import FeedbackForm
from medicine.models import Procedures, Feedback, Doctors


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['procedures_list'] = Procedures.objects.all()
        return context


class ProceduresListView(ListView):
    model = Procedures


class ProceduresDetailView(DetailView):
    model = Procedures


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DoctorsListView(ListView):
    model = Doctors


class ContactInfoView(TemplateView):
    template_name = "medicine/contact_info.html"
