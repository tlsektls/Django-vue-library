from django.shortcuts import render

# Create your views here.
#from django.views.generic.base import TemplateView
#from django.views import generic
from map.models import Map
from map.serializers import MapSerializer

from rest_framework import generics
from rest_framework.response import Response


#class MapView(generic.TemplateView):
#  model = Map
#  template_name = "body/map.html"

class MapView(generics.RetrieveAPIView):
  queryset = Map.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = MapSerializer(queryset,many=True)
    return Response(serializer.data)

