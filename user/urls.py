from django.urls import path
from user import views

urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('reg', views.reg),
    path('login_check', views.login_check),
    path('reg_check', views.reg_check),
    path('get_verify_img', views.get_verify_img),
]
