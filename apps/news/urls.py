#encoding: utf-8

from django.urls import path
from . import views
from django.shortcuts import reverse

# 设置app命名空间
app_name = 'news'

urlpatterns = [
    path('',views.index,name='index'),
]

# url反转：通过视图函数反转为url
# rever("news:index")