from django.db import models

# Create your models here.


class Comment(models.Model):
    """ 评论 """
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(verbose_name="评论内容", null=False)
    article = models.ForeignKey(verbose_name="文章", to='app_article.Article',
                                on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name="评论用户", to='app_users.User',
                             on_delete=models.CASCADE)
