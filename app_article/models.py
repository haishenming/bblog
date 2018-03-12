from django.db import models
from datetime import datetime
# Create your models here.


class Article(models.Model):
    """ 文章 """

    id = models.IntegerField(primary_key=True)
    title = models.CharField(verbose_name="标题", max_length=128,
                             null=False)
    content = models.TextField(verbose_name="内容", null=False)
    author = models.ForeignKey(verbose_name="作者", to='app_users.User',
                               on_delete=models.CASCADE)  # 文章作者
    tags = models.ManyToManyField(verbose_name="标签", to='Tag')

    category = models.ForeignKey(verbose_name="类别", to="Category",
                                 on_delete=models.SET_NULL, null=True,
                                 limit_choices_to={})

    created_time = models.DateTimeField(verbose_name="创建时间", null=False,
                                   auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="修改时间",
                                       null=True, auto_now=True)

    def __str__(self):
        return "{}-{}".format(self.title, self.author.username)


class Tag(models.Model):
    """ 标签 """
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=64, null=False, default="")
    user = models.ForeignKey(verbose_name="作者", to='app_users.User',
                               on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name="创建时间", null=False,
                                        auto_now=True)

    def __str__(self):
        return self.word


class Category(models.Model):
    """ 文章分类 """
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(verbose_name="作者", to='app_users.User',
                             on_delete=models.CASCADE)
    word = models.CharField(max_length=64, null=False, default="")

    created_time = models.DateTimeField(verbose_name="创建时间", null=False,
                                        auto_now=True)

    def __str__(self):
        return self.word

