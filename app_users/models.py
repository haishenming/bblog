from django.db import models
from django.contrib.auth.models import AbstractUser
from app_article.models import Article


# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(verbose_name="昵称", max_length=50,
                                blank=True)

    class Meta(AbstractUser.Meta):
        pass
