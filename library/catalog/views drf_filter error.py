from django.shortcuts import render
from .models import Book, Author, Publisher, BookInstance, Genre
from board.models import Map
from .serializers import BookSerializer,  BookInstanceSerializer, AuthorSerializer, PublisherSerializer

from rest_framework import generics, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import ModelMultipleChoiceFilter


class BookListView(generics.RetrieveAPIView):
  queryset = Book.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)



from django.forms.fields import MultipleChoiceField

class MultipleValueField(MultipleChoiceField):
  def __init__(self, *args, field_class, **kwargs):
    self.inner_field = field_class()
    super().__init__(*args, **kwargs)

  def valid_value(self, value):
    return self.inner_field.validate(value)

  def clean(self, values):
    return values and [self.inner_field.clean(value) for value in values]

from django_filters import rest_framework as filters
from django_filters.filters import Filter
#from django_filters import filters

class MultipleValueFilter(Filter):
    field_class = MultipleValueField

    def __init__(self, *args, field_class, **kwargs):
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, field_class=field_class, **kwargs)


from django.forms.fields import IntegerField

class ProductFilter(filters.FilterSet):
  id = MultipleValueFilter(field_class=IntegerField)
  #title = filters.CharFilter(lookup_expr='icontains')

  class Meta:
    model = Book
    fields = ['title']


class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  title = MultipleValueFilter(field_class=IntegerField)
  serializer_class = BookSerializer
  filter_backends = [DjangoFilterBackend]
  #filterset_fields = ['title']
  filterset_class = ProductFilter

