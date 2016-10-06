from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class Homepage(TemplateView):
	"""This a home page for marketing app
	"""
	template_name = 'marketing/home.html'