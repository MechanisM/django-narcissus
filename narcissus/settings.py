from django.conf import settings


STATIC_URL = getattr(settings, 'NARCISSUS_STATIC_URL', settings.STATIC_URL +
                     'narcissus/')

DEFAULT_FLOWERS = (
    'narcissus.flowers.UpdateFlower',
    'narcissus.flowers.ArticleFlower',
)
FLOWERS = getattr(settings, 'NARCISSUS_FLOWERS', DEFAULT_FLOWERS)
