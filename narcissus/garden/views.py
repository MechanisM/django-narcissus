from django.http import Http404
from django.views.generic import TemplateView
from django.views.generic.edit import BaseCreateView

from narcissus.garden import flowers
from narcissus.settings import STATIC_URL
from narcissus.utils.views import AjaxFormMixin


class HomeView(TemplateView):
    template_name = "narcissus/garden/home.html"

    def get_context_data(self, **kwargs):
        for name, flower in flowers.items():
            # Annotate each flower with an instance of the form that has
            # auto_id populated.
            form_class = flower.get_form_class()
            flower.form_instance = form_class(auto_id="id_%s_%%s" % name)
        
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'NARCISSUS_STATIC_URL': STATIC_URL,
            'user': self.request.user,
            'flowers': flowers,
        })
        return context


class PetalCreateView(AjaxFormMixin, BaseCreateView):
    http_method_names = ['post']
    template_name = "narcissus/garden/home.html"
    
    def post(self, request, petal):
        self.petal = petal
        try:
            flower = flowers[petal]
        except KeyError:
            raise Http404
        
        self.form_class = flower.form
        
        return super(PetalCreateView, self).post(request, petal)
