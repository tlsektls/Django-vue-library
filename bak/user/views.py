from django.shortcuts import render, redirect

from user.models import CustomUser
from user.serializers import UserSerializer



#from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


#class UserIndex(generics.RetrieveAPIView):
class UserIndex(APIView):
  queryset = CustomUser.objects.all()
  
  def get(self, request):
    queryset = self.get_queryset()
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

