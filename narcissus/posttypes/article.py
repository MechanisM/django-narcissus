from django.forms import ModelForm

from narcissus.posttypes.base import BasePostType
from narcissus.models import ArticlePost


class ArticleForm(ModelForm):

    class Meta:
        model = ArticlePost


class ArticlePostType(BasePostType):

    edit_template = 'narcissus/posts/article.html'
    model = ArticlePost
    form = ArticleForm

    def get_title(self):
        return self.instance.title

    def get_teaser(self):
        return self.instance.get_teaser(truncate=30)
