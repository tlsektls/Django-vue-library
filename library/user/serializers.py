from rest_framework import serializers
from .models import CustomUser
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.response import Response


#class UserRegistrationSerializer(TokenObtainPairSerializer):
class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        #fields = ('url', 'id', 'email', 'name', 'last_name', 'account_address', 'password', )
        fields = ('username', 'nikname', 'password')



class CutomObtainPairView(TokenObtainPairView):
    serializer_class = UserRegistrationSerializer

    #def post(self, request, *args, **kwargs):
    #    queryset = self.get_queryset()
    #    serializer = UserRegistrationSerializer(queryset,many=True)
    #    return Response(serializer.data)
  

#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = CustomUser
#        ordering = ['email', 'username']
#        fields = ['username', 'email', 'password']


