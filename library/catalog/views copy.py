from django.shortcuts import render
from .models import Book, Author, Publisher, BookInstance, Genre
from board.models import Map
from .serializers import BookSerializer,  BookInstanceSerializer, AuthorSerializer, PublisherSerializer

from rest_framework import generics, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import ModelMultipleChoiceFilter


def index(request):
  """View function for home page of site."""

  # Generate counts of some of the main objects
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()

  # Available books (status = 'a')
  num_instances_available = BookInstance.objects.filter(
  status__exact='a').count()

  # The 'all()' is implied by default.
  num_authors = Author.objects.count()


  # Number of visits to this view, as counted in the session variable.
  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1
  # 1씩 늘어나는것이 아니라 2씩 늘어남. 왜인지는 모름. 나중에 다시 고치기

	# 에세이라는 하나의 장르만 필터할 때
  num_genre_assai = Book.objects.filter(genre__name__contains='에세이').count()
	# 필터링 할때는 field_name__match_type 형식 사용
		# __icontains: 대소문자를 구분하지 않음
		# __iexact: 대소문자를 구분하지 않는 정확히 일치
		# __exact: 대소문자를 구분하는 정확한 일치
		# __startswith: 특정 문자로 시작

  #newsBoard의 가장 최신 글 5개 불러오기
  #result_5_news = NewsBoard.objects.order_by('-created_document_timestamp').first()

  #news = NewsBoard.objects.filter(datetime_attr__date=datetime.date(2022, 6, 26))
  #news = NewsBoard.objects.all()[:3]
  #images = BookImage.objects.all()

  address = Map.objects.all()

	# 장르별로 필터할 때
  string_genre_all = ''
  Genres = Genre.objects.all()
  for genre in Genres:
    count = Book.objects.filter(genre__name__contains=genre).count()
    string_genre_all += '<li><strong>{}:</strong> {}</li>'.format(genre, count)
  else : '<li><strong>등록된 장르가 없습니다.</strong></li>'
  

  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
		'num_genre_assai': num_genre_assai,
		'string_genre_all': string_genre_all,

    'num_visits': num_visits,
    #'images': images,
    'address': address,
    #'result_5_news': result_5_news,
  }

  # Render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)

#from django.views import generic

class BookListView(generics.RetrieveAPIView):
  queryset = Book.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)




class BookViewSet(viewsets.ModelViewSet):
  title = ModelMultipleChoiceFilter(
    name='title',
    lookup_expr='in',
    conjoined=True,  # uses AND instead of OR
  )
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  filter_backends = [DjangoFilterBackend] # 👈 DjangoFilterBackend 지정
  filterset_fields = ['title'] # 👈 filtering 기능을 사용할 field 입력


class BookFilter(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  #queryset = Book.objects.all().django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
  serializer_class = BookSerializer

  def get(self, request, *args, **kwargs):
    #가장 최신 글 5개 불러오기
    queryset = self.get_queryset()
    
    return queryset
    #return render(request, 'index.html', context=context)



class BookInstanceListView(generics.RetrieveAPIView):
  queryset = BookInstance.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = BookInstanceSerializer(queryset, many=True)
    return Response(serializer.data)


class AuthorListView(generics.RetrieveAPIView):
  queryset = Author.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = AuthorSerializer(queryset, many=True)
    return Response(serializer.data)


class PublisherListView(generics.RetrieveAPIView):
  queryset = Publisher.objects.all()
  
  def get(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = PublisherSerializer(queryset, many=True)
    return Response(serializer.data)
