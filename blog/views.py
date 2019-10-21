from django.shortcuts import render, redirect
from blog.models import BlogInfo
from django.http import HttpResponse, JsonResponse


# 定义登录判断装饰器
# 被装饰的函数执行之前执行
def login_required(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        if request.session.get('isLogin'):
            # 用户已登录
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录
            return redirect('/login')

    return wrapper


# Create your views here.
def index(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    blogs = BlogInfo.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs, 'username': username})


def login(request):
    if request.session.get('isLogin'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'blog/login_ajax.html', {'username': username})


# def login_check(request):
#     # request.POST 返回一个QueryDict 类似字典，但是这里键可以匹配多个值
#     # request.GET 返回一个QueryDict 匹配多值时用q.getlist('键')取出
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     print(username, password)
#     if username == 'hao' and password == 'hao':
#         return redirect('/index')
#     else:
#         return redirect('/login')
def login_check_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    print(username, password, remember)
    if username == 'hao' and password == 'hao':
        response = JsonResponse({'res': 1})
        if remember == 'true':
            print('remember is ' + str(remember))
            response.set_cookie('username', username, max_age=3600 * 5)
        request.session['isLogin'] = True
        return response
    else:
        return JsonResponse({'res': 0})


def reg(request):
    return render(request, 'blog/reg.html')


@login_required
def create(request):
    return render(request, 'blog/create.html')


@login_required
def delete(request, bid):
    blog = BlogInfo.objects.get(id=bid)
    blog.delete()
    return redirect('/index')
