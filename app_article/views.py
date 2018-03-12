import json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from app_article.models import Article

# Create your views here.

def article(requests, title):
    """ 文章 """
    article = Article.objects.filter(title=title).first()


    return render(requests, "article/article.html",
                  {
                      "article": article
                  })


def create(requests):
    """ 创建文章 """
    if requests.method == "POST":
        # 有文章数据上传
        user = requests.user
        article_data = requests.POST

    elif requests.method == "GET":
        # 返回创建页面
        return render(requests, 'article/create.html')