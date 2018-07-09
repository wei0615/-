#encoding: utf-8

from django.urls import path
from . import views

from django.shortcuts import reverse

# 设置app命名空间
app_name = 'cms'

urlpatterns = [
    path('',views.index,name='index'),
    path('write_news/',views.WriteNewsView.as_view(),name='write_news'),
    path('write_category/',views.news_category,name='news_category'),
    path('add_news_category/',views.add_news_category,name='add_news_category'),
    path('edit_news_category/',views.edit_news_category,name='edit_news_category'),
    path('delete_news_category/',views.delete_news_category,name='delete_news_category'),
    path('upload_file/',views.upload_file,name='upload_file'),

]

# url反转：通过视图函数反转为url
# rever("news:index")