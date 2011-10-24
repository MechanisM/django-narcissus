from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = _(u'category')
        verbose_name_plural = _(u'categories')
        ordering = ('title',)
    
    def __unicode__(self):
        return self.title


class Petal(models.Model):
    """
    A base model for the various content models to inherit from. The name of
    the model participates in the floral theme, each update becoming a petal on
    your beautiful narcissus flower.
    """

    CLOSED = 0
    DRAFT = 1
    LIVE = 2
    
    STATUS_CHOICES = (
        (CLOSED, _(u'Closed')),
        (DRAFT, _(u'Draft')),
        (LIVE, _(u'Live'))
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=LIVE,
        db_index=True,
    )    
    author = models.ForeignKey('auth.User', db_index=True)
    category = models.ForeignKey(Category, db_index=True)
    language = models.CharField(
        max_length=5,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    tags = TaggableManager()
    
    class Meta:
        verbose_name = _(u'petal')
        verbose_name_plural = _(u'petals')
        ordering = ('-date',)
    
    def __unicode__(self):
        return self.content.get_title()
