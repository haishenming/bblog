import json

import markdown

from django.shortcuts import render
from app_article.models import Article
from .forms import ArticeleForm

# Create your views here.

def article(requests, title):
    """ 文章 """
    this_article = Article.objects.filter(title=title).first()
    this_article.content = markdown.markdown(this_article.content)

    return render(requests, "article/article.html",
                  {
                      "article": this_article
                  })


def create(requests):
    """ 创建文章 """
    user = requests.user
    if requests.method == "POST":
        # 有文章数据上传
        article_form = ArticeleForm(user, requests.POST)

        if article_form.is_valid():
            this_article = article_form.save(commit=False)
            this_article.author = user
            this_article.save()

            return render(requests, 'article/create_done.html')
        else:
            raise ValueError(article_form.errors)

    # elif requests.method == "GET":
        # 返回创建页面
    else:
        article_form = ArticeleForm(user)

    return render(requests, 'article/create.html', {"form": article_form})