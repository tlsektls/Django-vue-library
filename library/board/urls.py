from django.urls import path
from board import views


urlpatterns = [
	path('map/', views.MapView.as_view(), name='map'),
	path('newsboard/', views.NewsBoardListView.as_view(), name='newsboard'),
	path('newsboard/news', views.ArticleListView.as_view(), name='news'),
]