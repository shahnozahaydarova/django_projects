from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name="index"),
    path('404', notfile, name="404"),
    path('about', about,name="about"),
    path('blog',blog,name="blog.html"),
    path('category',category,name="category.html"),
    path('base',contact,name='contact.html'),
    path('category',category,name="category.html"),
    path('contact',contact,name='contact-us.html'),
    path('login',login,name="login.html"),
    path('package',package,name="package.html"),
    path('register',register,name="register.html"),
    path('singleblog',singleblog,name="single-blog.html"),
    path('single',single,name="single.html"),
    path('store',store,name="store.html"),
    path('terms',terms,name="terms-conditions.html"),
    path('profile',profile,name="user-profile.html")
]
