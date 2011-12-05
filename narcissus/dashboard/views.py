from django.http import Http404
from django.views.generic import TemplateView
from django.views.generic.edit import BaseCreateView

from narcissus.dashboard import posttypes
from narcissus.settings import STATIC_URL
from narcissus.utils.views import AjaxFormMixin


class HomeView(TemplateView):
    template_name = "narcissus/dashboard/home.html"

    def get_context_data(self, **kwargs):
        for name, posttype in posttypes.items():
            # Annotate each flower with an instance of the form that has
            # auto_id populated.
            form_class = posttype.get_form_class()
            posttype.form_instance = form_class(auto_id="id_%s_%%s" % name)

        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'NARCISSUS_STATIC_URL': STATIC_URL,
            'user': self.request.user,
            'posttypes': posttypes,
        })
        return context


class PostCreateView(AjaxFormMixin, BaseCreateView):
    http_method_names = ['post']
    template_name = "narcissus/dashboard/home.html"

    def post(self, request, posttype_name):
        try:
            self.posttype = posttypes[posttype_name]
        except KeyError:
            raise Http404

        return super(PostCreateView, self).post(request, posttype_name)

    def get_form_class(self):
        return self.posttype.form
