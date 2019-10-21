from django.urls import path
from blog import views

urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('reg', views.reg),
    path('create', views.create),
    path('delete/<int:bid>', views.delete),
    path('login_check', views.login_check),
]
