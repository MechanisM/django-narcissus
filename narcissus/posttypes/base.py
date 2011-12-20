from django.forms import ModelForm
from django.forms.models import modelform_factory


class BasePostForm(ModelForm):

    class Meta:
        exclude = ('author', 'posttype')


class BasePostType(object):
    """
    PostType objects describe how the dashboard handles a particular post type.
    """

    # The template used when adding or editing a post.
    edit_template = 'narcissus/posts/edit.html'

    # The template used when displaying a post on the dashboard.
    view_template = 'narcissus/posts/view.html'

    model = None  # The model represented by the PostType.
    form = None  # The form used for new posts.

    def __init__(self, instance=None):
        # A post instance, used when displaying a post on the dashboard.
        self.instance = instance

    @classmethod
    def get_verbose_name(cls):
        """Convenience method to make it easy to retrieve the verbose name"""
        return str(cls.model._meta.verbose_name)

    @classmethod
    def get_verbose_name_plural(cls):
        """Convenience method to make it easy to retrieve the plural name"""
        return str(cls.model._meta.verbose_name_plural)

    @classmethod
    def get_form_class(cls):
        if cls.form is None:
            return modelform_factory(cls.model, form=BasePostForm)
        else:
            return cls.form
