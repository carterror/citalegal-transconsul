from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.contrib.admin.sites import site
from citas.models import Cita
# Create your views here.

class CustomView(TemplateView):
    template_name = "citas/aceptar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(site.each_context(self.request))
        ctx['cita'] = Cita.objects.get(pk=self.kwargs['pk'])
        return ctx
    