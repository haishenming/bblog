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