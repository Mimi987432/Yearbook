from django.urls import path

from authenticationapp import views
urlpatterns = [
    path('', views.homeregistration, name='homeregistration'),
    path('login', views.authlogin, name='authlogin'),
    path('logout',views.userlogout, name='userlogout'),
    
]