from django.urls import path
from blog import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login),
    path('reg', views.reg),
    path('create', views.create, name='create'),
    path('delete/<int:bid>', views.delete, name='delete'),
    path('login_check_ajax', views.login_check_ajax),
    path('get_verify_img', views.get_verify_img),
    path('upload', views.upload),
]
