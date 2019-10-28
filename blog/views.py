import markdown
from django.shortcuts import render, redirect
from blog.models import BlogInfo, AuthorInfo
from django.http import HttpResponse
# 上传文件导入settings
from django.conf import settings
from blog.models import BlogPicInfo, CategoryInfo, MDEditorForm


# 定义登录判断装饰器
# 被装饰的函数执行之前执行
def login_required(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        if request.session.get('isLogin'):
            # 用户已登录
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录
            return redirect('/user/login')

    return wrapper


# Create your views here.
def index(request):
    # 分页导入模块
    from django.core.paginator import Paginator

    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''

    blogs = BlogInfo.objects.all()
    paginator = Paginator(blogs, 4)  # 每页4条数据
    page = paginator.page(1)
    categories = CategoryInfo.objects.all()
    return render(request, 'blog/index.html',
                  {'blogs': blogs, 'categories': categories, 'username': username, 'page': page})


def show_blog(request, p_index):
    # 分页导入模块
    from django.core.paginator import Paginator
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    blogs = BlogInfo.objects.all()
    Paginator = Paginator(blogs, 4)  # 每页十条数据
    page = Paginator.page(p_index)
    return render(request, 'blog/index.html', {'blogs': blogs, 'username': username, 'page': page})


@login_required
def create(request):
    form = MDEditorForm()
    return render(request, 'blog/create.html', {'form': form})


@login_required
def delete(request, bid):
    blog = BlogInfo.objects.get(id=bid)
    blog.delete()
    return redirect('/')


@login_required
def update(request, bid):
    blog = BlogInfo.objects.get(id=bid)
    return render(request, 'blog/update.html', {'blog': blog})


@login_required
def change(request, bid):
    blog = BlogInfo.objects.get(id=bid)
    blog.b_title = request.POST.get('title')
    blog.b_content = request.POST.get('content')

    # 获取上传图片

    # 创建文件
    if request.FILES:
        pic = request.FILES['pic']
        save_path = '%s/blog/%s' % (settings.MEDIA_ROOT, pic.name)
        # 获取上传文件内容写到创建的文件中
        with open(save_path, 'wb') as f:
            for content in pic.chunks():
                f.write(content)
        # 数据库保存上传记录
        BlogPicInfo.objects.create(p_address='blog/%s' % pic.name)
        blog.b_pic = pic
    else:
        print('没有更改图片')
    blog.save()
    print('change')
    return redirect('/')


def detail(request, bid):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    blog = BlogInfo.objects.get(id=bid)
    blog.b_content = markdown.markdown(blog.b_content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    categories = CategoryInfo.objects.all()
    return render(request, 'blog/detail.html',
                  {'blog': blog, 'categories': categories, 'username': username})


# Create your views here.

def upload(request):
    """自定义上传"""
    # 获取上传图片
    pic = request.FILES['pic']
    # 创建文件
    save_path = '%s/blog/%s' % (settings.MEDIA_ROOT, pic.name)
    # 获取上传文件内容写到创建的文件中
    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)
    # 数据库保存上传记录
    BlogPicInfo.objects.create(p_address='blog/%s' % pic.name)
    print(save_path)
    # 返回上传结果
    return HttpResponse('ok')


def pub(request):
    print(request.POST)
    blog = BlogInfo()
    blog.b_title = request.POST.get('title')
    author_name = request.COOKIES['username']
    author_obj = AuthorInfo.objects.get(au_name=author_name)
    blog.b_author = author_obj
    blog.b_content = request.POST.get('content')

    """自定义上传博客图片"""
    # 获取上传图片
    cover = request.FILES['cover']
    # 创建文件
    save_path = '%s/blog/%s' % (settings.MEDIA_ROOT, cover.name)
    # 获取上传文件内容写到创建的文件中
    with open(save_path, 'wb') as f:
        for content in cover.chunks():
            f.write(content)
    # 数据库保存上传记录
    BlogPicInfo.objects.create(p_address='blog/%s' % cover.name)
    # 返回上传结果
    blog.b_cover = cover
    blog.save()
    return redirect('/')
