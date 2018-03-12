import json

import markdown

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from app_article.models import Article
from .forms import ArticeleForm

# Create your views here.

def article(requests, title):
    """ 文章 """
    article = Article.objects.filter(title=title).first()
    article.content = markdown.markdown(article.content)

    return render(requests, "article/article.html",
                  {
                      "article": article
                  })


def create(requests):
    """ 创建文章 """
    user = requests.user
    if requests.method == "POST":
        # 有文章数据上传
        article_form = ArticeleForm(user, requests.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = user
            article.save()

            return render(requests, 'article/create_done.html')
        else:
            raise ValueError(article_form.errors)

    # elif requests.method == "GET":
        # 返回创建页面
    else:
        article_form = ArticeleForm(user)

    return render(requests, 'article/create.html', {"form": article_form})