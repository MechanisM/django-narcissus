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
    
    def get_plural_name(self):
        return self.plural_name or self.name + 's'
    
    def get_long_name(self):
        return self.long_name or self.name
    
    def get_title(self, instance):
        """
        Gets the title that is used as the header for the content when it is
        displayed in the Garden.  Required.
        """
        raise NotImplementedError()
    
    def get_teaser(self, instance):
        """
        Gets the small block of text that is displayed under the header for the
        content when it is displayed in the Garden.  HTML can be used.
        """
        return None


class UpdateFlower(BaseFlower):
    
    name = 'update'
    long_name = 'status update'
    edit_template = 'narcissus/petals/status-update.html'
    
    def get_title(self, instance):
        return str(instance)


class ArticleFlower(BaseFlower):
    
    name = 'article'
    edit_template = 'narcissus/petals/article.html'
    
    def get_title(self, instance):
        return instance.title
    
    def get_teaser(self, instance):
        return instance.get_teaser(truncate=30)
