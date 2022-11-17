
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),

    path('user/', include('user.urls')),
    
    #path("rest-auth/", include('rest_auth.urls')),
    #path("rest-auth/registration/", include('rest_auth.registration.urls')),
]

## Use include() to add paths from the catalog application
#from django.conf.urls import include

#urlpatterns += [
#    path('catalog/', include('catalog.urls')),
#    path('map/', include('map.urls')),
#]

##Add URL maps to redirect the base URL to our application
#from django.views.generic import RedirectView

#urlpatterns += [
#    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
#]

# # Use static() to add url mapping to serve static files during development (only)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)