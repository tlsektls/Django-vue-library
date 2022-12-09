from django.urls import path, re_path
from catalog import views


urlpatterns = [
	path('', views.index, name='index'),

	path('books/', views.BookListView.as_view(), name='books'),

	path('bookSuggest/', views.BookSuggestView.as_view(), name='bookSuggest'),
	path('bookNew/', views.BookNewView.as_view(), name='bookNew'),
	#path('bookPopular/', views.BookPopularView.as_view(), name='bookPopular'),
	
	path('bookInstance/', views.BookInstanceListView.as_view(), name='booksInstance'),
	path('author/<int:pk>/', views.AuthorListView.as_view(), name='author'),
	path('publisher/', views.PublisherListView.as_view(), name='publisher'),
	

	path('genre/', views.GenreListView.as_view(), name='genre'),

	#path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]

