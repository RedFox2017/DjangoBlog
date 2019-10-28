from django.db import models


# Create your models here.
class BlogInfo(models.Model):
    b_title = models.CharField(verbose_name='博客标题', max_length=128)
    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
    # 此参数为了避免两个表里的数据不一致问题
    b_author = models.ForeignKey('AuthorInfo', on_delete=models.CASCADE)
    b_introduction = models.CharField(max_length=100)
    b_content = models.TextField()  # 博客内容
    b_pub_date = models.DateField(auto_now_add=True)
    b_upd_date = models.DateField(auto_now=True)
    b_pic = models.ImageField(upload_to='blog')

    def __str__(self):
        return self.b_title

    class Meta:
        db_table = 'blog_info'
        ordering = ['id']

    b_author.short_description = '作者'


class AuthorInfo(models.Model):
    au_name = models.CharField(verbose_name='作者', unique=True, max_length=48)
    au_id = models.CharField(max_length=24, blank=True)
    au_password = models.CharField(verbose_name='密码', max_length=48)
    au_email = models.CharField(verbose_name='邮箱', unique=True, max_length=100)

    def __str__(self):
        return self.au_name

    class Meta:
        db_table = 'author_info'


class BlogPicInfo(models.Model):
    p_address = models.ImageField(upload_to='blog')


class CategoryInfo(models.Model):
    c_name = models.CharField(unique=True, max_length=20)
    c_blog_num = models.IntegerField()
    c_blog = models.ManyToManyField(BlogInfo)

    def __str__(self):
        return self.c_name

    class Meta:
        db_table = 'category_info'
