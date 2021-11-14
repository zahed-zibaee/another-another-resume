# from django.shortcuts import render
from django.views.generic import TemplateView


class EnglishView(TemplateView):
    template_name = "resume/index.html"
