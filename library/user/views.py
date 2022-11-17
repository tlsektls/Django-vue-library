from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from user.models import User


from rest_framework import generics
from rest_framework.response import Response

class UserIndex(generics.RetrieveAPIView):
  queryset = User.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = BookInstanceSerializer(queryset, many=True)
    return Response(serializer.data)

