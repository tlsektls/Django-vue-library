from django.urls import path, re_path
from catalog import views


urlpatterns = [
	#path('', views.index, name='index'),

	path('catalog/', views.BookListView.as_view(), name='books'),
	path('bookInstance/', views.BookInstanceListView.as_view(), name='booksInstance'),
	
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	
#	path('catalog/', views.AuthorListView.as_view(), name='authors'),
#	path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

#	path('catalog/<int:pk>', views.PublisherDetailView.as_view(), name='publisher-detail'),

#	path('newsBoard/', views.NewsBoardListView.as_view(), name='newsBoard'),
#	path('newsBoard/<int:pk>', views.NewsBoardDetailView.as_view(), name='newsBoard-detail'),
]