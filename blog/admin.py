from django.contrib import admin
from blog.models import BlogInfo, AuthorInfo, BlogPicInfo


# Register your models here.
class BlogInfoAdmin(admin.ModelAdmin):
    """博客模型管理类"""
    list_per_page = 10
    list_display = ['b_title', 'b_author']
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ['b_title']
    search_fields = ['b_title']


admin.site.register(BlogInfo, BlogInfoAdmin)
admin.site.register(AuthorInfo)
admin.site.register(BlogPicInfo)
