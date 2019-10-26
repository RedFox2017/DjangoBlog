from django.db import models


# Create your models here.
class BlogInfo(models.Model):
    b_title = models.CharField(verbose_name='博客标题', max_length=128)
    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
    # 此参数为了避免两个表里的数据不一致问题
    b_author = models.ForeignKey('AuthorInfo', on_delete=models.CASCADE)
    b_content = models.TextField()
    b_pub_date = models.DateField(auto_now_add=True)
    b_upd_date = models.DateField(auto_now=True)
    b_pic = models.ImageField(upload_to='blog')

    def __str__(self):
        return self.b_title

    class Meta:
        db_table = 'bloginfo'
        ordering = ['id']

    b_author.short_description = '作者'


class AuthorInfo(models.Model):
    au_name = models.CharField(verbose_name='作者', max_length=48)
    au_id = models.CharField(max_length=24, blank=True)
    au_password = models.CharField(verbose_name='密码', max_length=48)

    def __str__(self):
        return self.au_name

    class Meta:
        db_table = 'authorinfo'


class BlogPicInfo(models.Model):
    p_address = models.ImageField(upload_to='blog')
