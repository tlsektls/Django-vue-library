
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


from user.models import CustomUser
from user.serializers import UserRegistrationSerializer
#from . import models
from django.db import models



class tokenUserView(APIView):
#  queryset = CustomUser.objects.all()
  
  def post(self, request):
    #queryset = self.get_queryset()
    #serializer = UserRegistrationSerializer(queryset, many=True)
    nikname = CustomUser.objects.create_user(username=request.data['id'], password=request.data['password'])
    print(request.nikname)

    token = Token.objects.create(nikname=nikname)
    return Response({"Token": token.key})

#class SignupView(APIView):
#    def post(self, request):
#        nikname = CustomUser.objects.create_user(username=request.data['id'], password=request.data['password'])

#        nikname.save()

#        token = Token.objects.create(nikname=nikname)
#        return Response({"Token": token.key})