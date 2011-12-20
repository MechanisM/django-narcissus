from narcissus.posttypes.base import BasePostType
from narcissus.models import ArticlePost


class ArticlePostType(BasePostType):

    edit_template = 'narcissus/posts/article.html'
    model = ArticlePost
