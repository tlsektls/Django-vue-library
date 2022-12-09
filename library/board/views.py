from django.shortcuts import render

# Create your views here.
#from django.views.generic.base import TemplateView
#from django.views import generic
from .models import Map, OffDay, NewsBoard
from .serializers import MapSerializer, OffDaySerializer, NewsBoardSerializer

from rest_framework import generics
from rest_framework.response import Response


#class MapView(generic.TemplateView):
#  model = Map
#  template_name = "body/map.html"

class MapView(generics.GenericAPIView):
  queryset = Map.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = MapSerializer(queryset,many=True)
    return Response(serializer.data)


class OffDayView(generics.GenericAPIView):
  queryset = OffDay.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = OffDaySerializer(queryset,many=True)
    return Response(serializer.data)


class NewsBoardListView(generics.GenericAPIView):
  queryset = NewsBoard.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = NewsBoardSerializer(queryset,many=True)
    return Response(serializer.data)
  
  #def post(self, request, *args, **kwargs):
  #  queryset = NewsBoard.objects.filter(id=self.id)
  #  serializer = NewsBoardSerializer(queryset,many=True)
    #return Response(serializer.data)


class NewsBoardOneView(generics.RetrieveAPIView):
  queryset = NewsBoard.objects.all()
  serializer_class = NewsBoardSerializer

