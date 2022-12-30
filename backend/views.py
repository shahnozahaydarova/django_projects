from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def notfile(request):
    return render(request,'404.html')

def about(request):
    return render(request,'about-us.html')

def ad_list(request):
    return render(request,'ad-list-view.html')

def ad_listing(request):
    return render(request,'ad-listing.html')

def blog(request):
    return render(request,'blog.html')

def category(request):
    return render(request,'category.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def package(request):
    return render(request,'package.html')

def register(request):
    return render(request,'register.html')

def singleblog(request):
    return render(request,'single-blog.html')

def single(request):
    return render(request,'single.html')

def store(request):
    return render(request,'store.html')

def terms(request):
    return render(request,'terms-condition.html')

def profile(request):
    return render(request,'user-profile.html')