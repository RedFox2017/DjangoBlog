from django.contrib import admin
from blog.models import BlogInfo, AuthorInfo

# Register your models here.
admin.site.register(BlogInfo)
admin.site.register(AuthorInfo)
