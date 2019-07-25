# chat/urls.py
from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('small_screen', views.small_screen, name='small_screen'),
    path('recording', views.recording, name='recording'),
    path('small_screen_2', views.small_screen_2, name='small_screen_2'),
  

]

