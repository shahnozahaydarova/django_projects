from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('404', notfile, name="404.html"),
    path('about', about,name="about.html"),
    path('adlist',ad_list,name="adlist.html"),
    path('adlisting',ad_listing,name="adlisting.html"),
    path('blog',blog,name="blog.html"),
    path('category',category,name="category.html"),
    path('base',contact,name='contact.html'),
]
