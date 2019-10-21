from django.db import models


# Create your models here.
class BlogInfo(models.Model):
    b_title = models.CharField(max_length=128)
    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
    # 此参数为了避免两个表里的数据不一致问题
    b_author = models.ForeignKey('AuthorInfo', on_delete=models.CASCADE)
    b_content = models.TextField()
    b_pub_date = models.DateField(auto_now_add=True)
    b_upd_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.b_title

    class Meta:
        db_table = 'bloginfo'


class AuthorInfo(models.Model):
    au_name = models.CharField(max_length=48)
    au_id = models.CharField(max_length=24)

    def __str__(self):
        return self.au_name

    class Meta:
        db_table = 'authorinfo'
