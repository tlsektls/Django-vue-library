from django.shortcuts import render

# Create your views here.
#from django.views.generic.base import TemplateView
from django.views import generic
from map.models import Map


class MapView(generic.TemplateView):
  model = Map
  template_name = "body/map.html"