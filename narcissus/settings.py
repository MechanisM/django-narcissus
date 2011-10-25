from django.conf import settings


STATIC_URL = getattr(settings, 'NARCISSUS_STATIC_URL', settings.STATIC_URL +
                     'narcissus/')
