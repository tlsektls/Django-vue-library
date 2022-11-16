from django.db import models
from django.urls import reverse

import requests, json

# Create your models here.

class MyModelName(models.Model):
  """A typical class defining a model, derived from the Model class."""

  # Fields
  my_field_name = models.CharField(
      max_length=20, help_text='Enter field documentation')

# Metadata

class Meta:
	ordering = ['title', '-my_field_name']
  
	# Methods
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of MyModelName."""
		return reverse('model-detail-view', args=[str(self.id)])

	def __str__(self):
		"""String for representing the MyModelName object (in Admin site etc.)."""
		return self.field_name



class Map(models.Model):
    """Model Map"""
    address = models.TextField(default="")
    latitude = models.IntegerField(default="0")
    longitude = models.IntegerField(default="0")

    #def get_location(add):
    #    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + add
    #    headers = {"Authorization": "KakaoAK 	e704ab6e9bd82a9c42c124931e6f5051"}
    #    api_json = json.loads(str(requests.get(url,headers=headers).text))
    #    addre = api_json['documents'][0]['address']
    #    coor = {"lat": str(addre['y']), "lng": str(addre['x'])}
    #    address_name = addre['address_name']

    #    return coor

    #coordinate = get_location(address)


    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f'{self.address}, {self.latitude}, {self.longitude}'