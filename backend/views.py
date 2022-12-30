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
