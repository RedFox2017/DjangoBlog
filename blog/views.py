from django.shortcuts import render, redirect
from blog.models import BlogInfo
from django.http import HttpResponse


# Create your views here.
def index(request):
    blogs = BlogInfo.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})


def login(request):
    return render(request, 'blog/login.html')


def login_check(request):
    # request.POST 返回一个QueryDict 类似字典，但是这里键可以匹配多个值
    # request.GET 返回一个QueryDict 匹配多值时用q.getlist('键')取出
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    if username == 'hao' and password == 'hao':
        return redirect('/index')
    else:
        return redirect('/login')


def reg(request):
    return render(request, 'blog/reg.html')


def create(request):
    return render(request, 'blog/create.html')


def delete(request, bid):
    blog = BlogInfo.objects.get(id=bid)
    blog.delete()
    return redirect('/index')
