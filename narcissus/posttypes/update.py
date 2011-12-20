from django.utils.text import truncate_words

from narcissus.posttypes.base import BasePostType
from narcissus.models import UpdatePost


class UpdatePostType(BasePostType):

    edit_template = 'narcissus/posts/update.html'
    model = UpdatePost
