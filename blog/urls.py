from django.urls import path
from blog import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login),
    path('logout', views.logout),
    path('reg', views.reg),
    path('create', views.create, name='create'),
    path('delete/<int:bid>', views.delete, name='delete'),
    path('login_check_ajax', views.login_check_ajax),
    path('get_verify_img', views.get_verify_img),
    path('upload', views.upload),
    path('show_blog/<int:p_index>', views.show_blog),
    path('pub', views.pub),
]
