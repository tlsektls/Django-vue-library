from django.db import models
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.

class Map(models.Model):
    """Model Map"""
    address = models.TextField(default="")
    latitude = models.FloatField(default="0")
    longitude = models.FloatField(default="0")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f'{self.address}, {self.latitude}, {self.longitude}'


class OffDay(models.Model):
    """Model Map"""
    day_title = models.CharField(max_length=7, null=True, blank=True)
    offday = models.DateField(default=now)

    def __str__(self):
        return f'{self.day_title} ({self.offday})'


class NewsBoard(models.Model):
  """Model representing an NewsBoard."""
  news_title = models.TextField(default="도서관 뉴스")
  news_date = models.DateField(default=now)
  news_content = models.TextField(default="", null=True, blank=True)
  news_poster = models.ImageField(null=True, upload_to="newsborad/", blank=True)
  def get_news_poster(self, car):
    request = self.context.get('request')
    news_poster = self.image.url
    return request.build_absolute_uri(news_poster)

  #id = models.AutoField(primary_key=True)

  class Meta:
    ordering = ['-news_date', 'news_title']

  def get_absolute_url(self):
    """Returns the url to access a particular author instance."""
    return reverse('newsboard/news', args=[str(self.id)])

  def __str__(self):
    return self.news_title


class SuggestBoard(models.Model):
  """Model representing an NewsBoard."""
  suggest_title = models.TextField(default="도서관 뉴스")
  suggest_date = models.DateField(default=now)
  suggest_content = models.TextField(default="", null=True, blank=True)

  #id = models.AutoField(primary_key=True)

  class Meta:
    ordering = ['-suggest_date', 'suggest_title']

  def get_absolute_url(self):
    """Returns the url to access a particular author instance."""
    return reverse('suggestboard/suggest', args=[str(self.id)])

  def __str__(self):
    return self.newsuggest_titles_title
