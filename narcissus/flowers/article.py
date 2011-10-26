from narcissus.flowers.base import BaseFlower
from narcissus.models import ArticlePetal


class ArticleFlower(BaseFlower):
    
    name = 'article'
    edit_template = 'narcissus/petals/article.html'
    petal = ArticlePetal
    
    def get_title(self):
        return self.instance.title
    
    def get_teaser(self):
        return self.instance.get_teaser(truncate=30)
