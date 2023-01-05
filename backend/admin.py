from django.contrib import admin
from .models import *

@admin.register(MaishiyTehnikalar)
class ArticleAsosiyMahsulotlar(admin.ModelAdmin):
    list_display=('name','date',)
    list_filter=('content',)

@admin.register(Mebellar)
class ArticleAsosiyMahsulotlar(admin.ModelAdmin):
    list_display=('name','date',)
    list_filter=('content',)


@admin.register(BarchaToifalar)
class ArticleBarchaToifalar(admin.ModelAdmin):
    list_display=('name',)