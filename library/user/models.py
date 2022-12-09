from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

  #class Meta:
  #  managed = False
    #db_table = 'user'

  def __str__(self):
    return self.username

