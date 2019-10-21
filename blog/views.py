from django.shortcuts import render,redirect
from blog.models import BlogInfo


# Create your views here.
def index(request):
    blogs = BlogInfo.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})


def login(request):
    return render(request, 'blog/login.html')


def reg(request):
    return render(request, 'blog/reg.html')


def create(request):
    return render(request, 'blog/create.html')


def delete(request, bid):
    blog = BlogInfo.objects.get(id=bid)
    blog.delete()
    return redirect('/')
