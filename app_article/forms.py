from django import forms
from pagedown.widgets import AdminPagedownWidget

from .models import Article, Category, Tag


class ArticeleForm(forms.ModelForm):
    """ 文章表单 """
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设返回当前属于当前用户的category和tags
        self.fields['category'].queryset = Category.objects.filter(
            user=user)
        self.fields['tags'].queryset = Tag.objects.filter(
            user=user)
        self.fields['tags'].required = False
        self.fields['content'].widget = AdminPagedownWidget()

    class Meta:
        model = Article
        fields = ["title", "content", "category", "tags"]



