from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name="index"),
    path('404', notfile, name="404"),
    path('about', about,name="about"),
    path('category',category,name="category.html"),
    path('base',contact,name='contact.html'),
    path('category',category,name="category.html"),
    path('contact',contact,name='contact-us.html'),
    path('login',login,name="login.html"),
    path('register',register,name="register.html"),
    path('store',store,name="store.html"),
]
