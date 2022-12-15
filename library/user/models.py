from django.db import models
from catalog.models import BookInstance
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.base_user import AbstractBaseUser

class CustomUser(AbstractUser):
  nikname = models.CharField(max_length=8, help_text='8자 이내로 이름을 작성해주세요')
  #email = 'username'
  REQUIRED_FIELDS = ['nikname', 'password']
  USERNAME_FIELD = 'username'
  #REQUIRED_FIELDS = ['email', 'nikname', 'password']
  #USERNAME_FIELD = 'username'

  #borrowBook = ArrayField(ArrayField(models.IntegerField(null=True,blank=True), size=8, ), size=8, )
    

  class Meta:
    ordering = ['username', 'nikname']

  def __str__(self):
    return self.username


  #class Meta:
  #  managed = False
    #db_table = 'user'

  #def __str__(self):
  #  return self.username
