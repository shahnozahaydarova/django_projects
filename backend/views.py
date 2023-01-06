from django.shortcuts import render
from .models import *

def home(request):
    ams = MaishiyTehnikalar.objects.all()
    ms = Mebellar.objects.all()
    bts = BarchaToifalar.objects.all()
    context = {
        'ams':ams,
        'ms':ms,
        'bts':bts
    }
    return render(request,'index.html',context)

def notfile(request):
    return render(request,'404.html')

def about(request):
    return render(request,'about-us.html')


def blog(request):
    return render(request,'blog.html')

def category(request):
    mts = MaishiyTehnikalar.objects.all()
    ms = Mebellar.objects.all()
    mtss = MaishiyTehnikalarSoni.objects.all()
    mss = MebellarSoni.objects.all()
    context = {
        'mts': mts,
        'ms':ms,
        'mtss':mtss,
        'mss':mss,
    }
    return render(request,'category.html',context)

def contact(request):
    mts = MaishiyTehnikalar.objects.all()
    ms = Mebellar.objects.all()
    context = {
        'mts': mts,
        'ms':ms,
    }
    return render(request,'contact-us.html',context)

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