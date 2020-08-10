from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class StartView(TemplateView):
    template_name = "accounting_start.html"
