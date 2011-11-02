from django.forms import ModelForm

from narcissus.flowers.base import BaseFlower
from narcissus.models import UpdatePetal


class UpdateForm(ModelForm):
    class Meta:
        model = UpdatePetal


class UpdateFlower(BaseFlower):
    
    name = 'update'
    long_name = 'status update'
    edit_template = 'narcissus/petals/update.html'
    petal = UpdatePetal
    form = UpdateForm
    
    def get_title(self):
        return str(self.instance)
