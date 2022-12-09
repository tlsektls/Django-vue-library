
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf.urls.static import static
from django.conf import settings

from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),

    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),


	path('map/', views.MapView.as_view(), name='map'),
	path('offday/', views.OffDayView.as_view(), name='offday'),
	path('newsboard/', views.NewsBoardListView.as_view(), name='newsboard'),

	path('newsboard/news/<int:pk>/', views.NewsBoardOneView.as_view(), name='newsboard-news'),

    #path('user/', include('user.urls')),
    #path("user-auth/", include("rest_framework.urls")),

]

# # Use static() to add url mapping to serve static files during development (only)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)