from django.urls import path
 
from user import views
 
urlpatterns = [
	path('login/', views.UserIndex.as_view(), name='login'),
    #path('register/', views.user_reg, name='user_reg'),
    #path('login/', views.user_login, name='user_login'),
    #path('logout/', views.user_logout, name='user_logout'),
]
