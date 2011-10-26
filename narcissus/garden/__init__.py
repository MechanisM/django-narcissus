from django.conf import settings
from django.utils.importlib import import_module

from narcissus.settings import FLOWERS

# Cache of actual flower classes.
_narcissus_flowers = None


def _get_flowers():
    global _narcissus_flowers
    if _narcissus_flowers is None:
        flowers = []
        for path in FLOWERS:
            i = path.rfind('.')
            module, attr = path[:i], path[i+1:]
            try:
                mod = import_module(module)
            except ImportError, e:
                raise ImproperlyConfigured('Error importing narcissus flower module %s: "%s"' % (module, e))
            try:
                flower = getattr(mod, attr)
            except AttributeError:
                raise ImproperlyConfigured('Module "%s" does not define a "%s" flower class' % (module, attr))
            flowers.append(flower)
        _narcissus_flowers = flowers
    return _narcissus_flowers

flowers = _get_flowers()
