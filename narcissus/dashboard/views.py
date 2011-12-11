from django.http import Http404
from django.views.generic import TemplateView
from django.views.generic.edit import BaseCreateView, BaseDeleteView

from narcissus.dashboard import posttypes
from narcissus.settings import STATIC_URL
from narcissus.utils.views import AjaxModelFormMixin, AjaxDeletionMixin


class HomeView(TemplateView):
    template_name = "narcissus/dashboard/home.html"

    def get_context_data(self, **kwargs):
        for name, posttype in posttypes.items():
            # Annotate each posttype with an instance of the form that has
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


class PostCreateView(AjaxModelFormMixin, BaseCreateView):

    def post(self, request, posttype_name):
        try:
            self.posttype = posttypes[posttype_name]
        except KeyError:
            raise Http404

        return super(PostCreateView, self).post(request, posttype_name)

    def get_form_class(self):
        return self.posttype.get_form_class()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostDeleteView(AjaxDeletionMixin, BaseDeleteView):

    def delete(self, request, posttype_name, *args, **kwargs):
        try:
            self.posttype = posttypes[posttype_name]
        except KeyError:
            raise Http404

        self.queryset = self.posttype.model.objects.all()

        return super(PostDeleteView, self).delete(request, posttype_name,
                                                  *args, **kwargs)
