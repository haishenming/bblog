import json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from app_users.models import User


# Create your views here.

def article(requests, title):
    """ 文章 """

    return HttpResponse("这是文章{}".format(title))