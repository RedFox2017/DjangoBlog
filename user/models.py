from django.db import models


# Create your models here.
class UserInfo(models.Model):
    u_name = models.CharField(verbose_name='作者', unique=True, max_length=48)
    u_id = models.CharField(max_length=24, blank=True)
    u_password = models.CharField(verbose_name='密码', max_length=48)
    u_email = models.CharField(verbose_name='邮箱', unique=True, max_length=100)

    def __str__(self):
        return self.u_name

    class Meta:
        db_table = 'user_info'
