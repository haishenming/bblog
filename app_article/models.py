from django.db import models

# Create your models here.


class Article(models.Model):
    """ 文章 """
    id = models.IntegerField(primary_key=True)
    title = models.CharField(verbose_name="标题", max_length=128,
                             null=False)
    content = models.TextField(verbose_name="内容", null=False)
    author = models.ForeignKey(verbose_name="作者", to='app_users.User',
                               on_delete=models.CASCADE)  # 文章作者
