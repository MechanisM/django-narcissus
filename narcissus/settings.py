from django.conf import settings


STATIC_URL = getattr(settings, 'NARCISSUS_STATIC_URL', settings.STATIC_URL +
                     'narcissus/')

DEFAULT_POSTTYPES = (
    'narcissus.posttypes.update.UpdatePostType',
    'narcissus.posttypes.article.ArticlePostType',
)
POSTTYPES = getattr(settings, 'NARCISSUS_POSTTYPES', DEFAULT_POSTTYPES)
