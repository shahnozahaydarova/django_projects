from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('404', notfile, name="404"),
    path('about', about,name="about"),
    path('adlist',ad_list,name="adlist")
]
