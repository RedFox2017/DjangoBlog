from django.db import models


# Create your models here.
class BlogInfo(models.Model):
    b_title = models.CharField(max_length=128)
    b_author = models.CharField(max_length=50)
    b_content = models.TextField()
    b_pub_date = models.DateField(auto_now=True)
    b_upd_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.b_title


class AuthorInfo(models.Model):
    au_name = models.CharField(max_length=48)
    au_id = models.CharField(max_length=24)

    def __str__(self):
        return self.au_name
