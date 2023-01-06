from django.contrib import admin
from .models import *

@admin.register(MaishiyTehnikalar)
class ArticleAsosiyMahsulotlar(admin.ModelAdmin):
    list_display=('name','date',)


@admin.register(Mebellar)
class ArticleAsosiyMahsulotlar(admin.ModelAdmin):
    list_display=('name','date',)


@admin.register(BarchaToifalar)
class ArticleBarchaToifalar(admin.ModelAdmin):
    list_display=('name',)



@admin.register(MaishiyTehnikalarSoni)
class ArticleBarchaToifalar(admin.ModelAdmin):
    list_display=('name',)



@admin.register(MebellarSoni)
class ArticleBarchaToifalar(admin.ModelAdmin):
    list_display=('name',)