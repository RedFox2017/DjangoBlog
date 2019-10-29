from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('delete/<int:bid>', views.delete, name='delete'),
    path('detail/<int:bid>', views.detail, name='detail'),
    path('update/<int:bid>', views.update, name='update'),
    path('change/<int:bid>', views.change, name='change'),
    path('upload', views.upload),
    path('show_blog/<int:p_index>', views.show_blog),
    path('pub', views.pub),
    path('search', views.search),
    path('tips', views.tips),
    path('category/<int:cid>', views.category, name='category'),
]
