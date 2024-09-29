from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from medicine.models import Procedures


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
