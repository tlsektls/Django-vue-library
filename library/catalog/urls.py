from django.urls import path, re_path
from catalog import views


urlpatterns = [
	path('', views.index, name='index'),

	path('book/', views.BookListView.as_view(), name='books'),
	path('bookInstance/', views.BookInstanceListView.as_view(), name='booksInstance'),
	path('author/', views.AuthorListView.as_view(), name='author'),
	path('publisher/', views.PublisherListView.as_view(), name='publisher'),
	path('newsboard/', views.NewsBoardListView.as_view(), name='newsboard'),
	
	#path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	

]

