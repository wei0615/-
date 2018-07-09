from django.shortcuts import render

# 通过视图函数找其对应的url，那么这种就叫做url反转
# 通过url来找到视图函数

def index(request):
    return render(request,'news/index.html')


