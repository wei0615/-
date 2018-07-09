from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.views.generic import View
from apps.news.models import *
from utils import restful
from .forms import *
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@staff_member_required(login_url='/')
def index(request):
    return render(request,'cms/index.html')

@method_decorator(login_required(login_url='/account/login/'),name='dispatch')
class WriteNewsView(View):
    def get(self,request):
        categories = NewsCategory.objects.all()
        return render(request,'cms/write_news.html',context={
            'categories':categories,
        })

    def post(self,request):
        form = WriteNewsForms(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            category = News.objects.filter(pk=category_id)
            News.objects.create(title=title,desc=desc,thumbnail=thumbnail,content=content,category=category,author=request.user)

            return restful.ok()
        else:
            return restful.params_error(message=form.get_error())

def news_category(request):
    categories = NewsCategory.objects.order_by('-id')
    return render(request,'cms/news_category.html',context={
        'categories':categories,
    })

@require_POST
def add_news_category(request):
    name = request.POST.get('name')
    exists= NewsCategory.objects.filter(name=name).exists()
    if not exists:
        NewsCategory.objects.create(name=name)
        return restful.ok()
    else:
        return restful.params_error(message='该分类已经存在！')

@require_POST
def edit_news_category(request):
    form = EditNewsCategoryForms(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get('pk')
        name = form.cleaned_data.get('name')
        try:
            NewsCategory.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error(message='分类不存在')
    else:
        return restful.params_error(message=form.get_error())

@require_POST
def delete_news_category(request):
    pk = request.POST.get('pk')
    try:
        NewsCategory.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.params_error(message='该分类不存在')

@require_POST
def upload_file(request):
    file = request.FILES.get('upfile')
    name = file.name
    filepath = os.path.join(settings.MEDIA_ROOT,name)
    with open(filepath,'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    url = request.build_absolute_uri(settings.MEDIA_URL+name)
    return restful.result(data={"url":url})





