from django.forms import ModelForm

from narcissus.posttypes.base import BasePostType
from narcissus.models import UpdatePost


class UpdateForm(ModelForm):
    
    class Meta:
        model = UpdatePost


class UpdatePostType(BasePostType):
    
    edit_template = 'narcissus/posts/update.html'
    model = UpdatePost
    form = UpdateForm
    
    def get_title(self):
        return str(self.instance)
