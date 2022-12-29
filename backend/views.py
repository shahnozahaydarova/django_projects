from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def notfile(request):
    return render(request,'404.html')
def about(request):
    return render(request,'about-us.html')

def ad_list(request):
    return render(request,'ad-list-view.html')
