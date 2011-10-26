class BaseFlower(object):
    """
    A Flower is a content type, and each entry in the content type is called a
    petal.  Flower objects describe how the Garden (the user dashboard) handles
    a particular content type.
    """
    
    name = None  # The name of the content type the Flower represents.
    plural_name = None  # An optional plural form of the name.
    long_name = None  # An optional longer form of the name.
    
    # The template used when adding or editing a petal.
    edit_template = 'narcissus/petals/edit.html'
    
    # The template used when displaying a petal in the Garden.
    view_template = 'narcissus/petals/view.html'
    
    petal = None  # The petal model used by the Flower.
    
    def __init__(self, instance=None):
        # A petal instance, used when displaying a petal in the Garden.
        self.instance = instance
    
    @classmethod
    def get_plural_name(cls):
        return cls.plural_name or cls.name + 's'
    
    @classmethod
    def get_long_name(cls):
        return cls.long_name or cls.name
    
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
