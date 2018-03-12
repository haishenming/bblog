from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget

from .models import Article, Category, Tag
from django import forms


# Register your models here.

# Register your models here.
# 定义自己的form

class ArticeleForm(forms.ModelForm):
    """ 文章表单 """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget = AdminPagedownWidget()
        self.fields['tags'].required = False

    class Meta:
        model = Article
        exclude = []


class ArticleAdmin(admin.ModelAdmin):
    form = ArticeleForm


admin.site.register(Article, ArticleAdmin)
