from django.forms.models import modelform_factory

class BaseFlower(object):
    """
    A Flower is a content type, and each entry in the content type is called a
    Petal.  Flower objects describe how the Garden (the user dashboard) handles
    a particular content type.
    """
    
    # The template used when adding or editing a petal.
    edit_template = 'narcissus/petals/edit.html'
    
    # The template used when displaying a petal in the Garden.
    view_template = 'narcissus/petals/view.html'
    
    petal = None  # The petal model used by the Flower.
    form = None  # The form used for new {etals.
    
    def __init__(self, instance=None):
        # A petal instance, used when displaying a petal in the Garden.
        self.instance = instance
    
    @classmethod
    def get_verbose_name(cls):
        """Convenience method to make it easy to retrieve the verbose name"""
        return str(cls.petal._meta.verbose_name)
    
    @classmethod
    def get_verbose_name_plural(cls):
        """Convenience method to make it easy to retrieve the plural name"""
        return str(cls.petal._meta.verbose_name_plural)
    
    @classmethod
    def get_form_class(cls):
        if cls.form is None:
            return modelform_factory(cls.petal)
        else:
            return cls.form
    
    def get_title(self):
        """
        Gets the title that is used as the header for the content when it is
        displayed in the Garden.  Required.
        """
        raise NotImplementedError()
    
    def get_teaser(self):
        """
        Gets the small block of text that is displayed under the header for the
        content when it is displayed in the Garden.  HTML can be used.
        """
        return None
