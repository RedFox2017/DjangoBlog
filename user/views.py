from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from blog.models import AuthorInfo

# 生成验证码导入模块
import random
import io
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image


# Create your views here.

def login(request):
    if request.session.get('isLogin'):
        return redirect('/')
    else:
        if 'remember_name' in request.COOKIES:
            remember_name = request.COOKIES['remember_name']
        else:
            remember_name = ''
        return render(request, 'user/login.html', {'remember_name': remember_name})


def logout(request):
    request.session.clear()
    response = redirect('/')
    response.delete_cookie('username')
    return response

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


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    c_code = request.POST.get('verify_code')
    s_code = request.session.get("code")
    print(username, password)
    user = AuthorInfo.objects.filter(au_name=username, au_password=password)  # 此时不会执行查询
    # 从session获取的
    print(user, remember)
    if s_code.lower() == c_code.lower():
        if user:
            response = JsonResponse({'res': 1})
            if remember == 'true':
                response.set_cookie('remember_name', username)
            else:
                response.set_cookie('remember_name', '')
            response.set_cookie('username', username, max_age=3600 * 5)
            request.session['isLogin'] = True
            return response
        else:
            return JsonResponse({'res': 0})
    else:
        return JsonResponse({'res': -1})


def reg(request):
    return render(request, 'user/reg.html')


def reg_check(request):
    name = request.POST.get('username')
    email = request.POST.get('email')
    pwd = request.POST.get('password')
    re_pwd = request.POST.get('re_pwd')
    if pwd == re_pwd:
        has_exit = AuthorInfo.objects.filter(au_name=name)
        if has_exit:
            return JsonResponse({'res': -1})
        else:
            author = AuthorInfo()
            author.au_name = name
            author.au_email = email
            author.au_password = pwd
            author.save()
            print('注册成功')
            return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


# 获取随机颜色
def get_random_color():
    R = random.randrange(255)
    G = random.randrange(255)
    B = random.randrange(255)
    return (R, G, B)


def get_verify_img(req):
    # 定义画布背景颜色
    bg_color = get_random_color()
    # 画布大小
    img_size = (100, 44)
    # 定义画布
    image = Image.new("RGB", img_size, bg_color)
    # 定义画笔
    draw = ImageDraw.Draw(image, "RGB")
    # 创建字体（字体的路径，服务器路径）
    font_path = 'static/fonts/AdobeArabic-BoldItalic.otf'
    # 实例化字体，设置大小是30
    font = ImageFont.truetype(font_path, 40)
    # 准备画布上的字符集
    source = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
    # 保存每次随机出来的字符
    code_str = ""
    for i in range(4):
        # 获取数字随机颜色
        text_color = get_random_color()
        # 获取随机数字 len
        tmp_num = random.randrange(len(source))
        # 获取随机字符 画布上的字符集
        random_str = source[tmp_num]
        # 将每次随机的字符保存（遍历） 随机四次
        code_str += random_str
        # 将字符画到画布上
        draw.text((10 + 20 * i, 2), random_str, text_color, font)
        draw.line(((1, random.randint(1, 44)), (100, random.randint(1, 40))), get_random_color(), 1)
    # 记录给哪个请求发了什么验证码
    req.session['code'] = code_str

    # 使用画笔将文字画到画布上
    # draw.text((10, 20), "X", text_color, font)
    # draw.text((40, 20), "Q", text_color, font)
    # draw.text((60, 20), "W", text_color, font)
    del draw
    # 获得一个缓存区
    buf = io.BytesIO()
    # 将图片保存到缓存区
    image.save(buf, 'png')
    # 将缓存区的内容返回给前端 .getvalue 是把缓存区的所有数据读取
    return HttpResponse(buf.getvalue(), 'image/png')
