from django.urls import path

from achievement import views
urlpatterns = [
    path('', views.homeachievement, name='homeachievement'),
    path('seeachievement', views.seeachievement, name='seeachievement'),
    path('addachievement', views.addachievement, name='addachievement'),
    
]