import json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from app_users.models import User


# Create your views here.


class ArticleView(View):
    """ 文章视图 """

    def get(self, requests):
        """ 获取文章 """
        datas = requests.GET

        username = datas.get("username")
        if username:
            articles = User.objects.filter(article__author=username)
        else:
            return HttpResponse(json.dumps({}))

        # for article in articles:
        #     rdata =


        return HttpResponse(json.dumps({}))
