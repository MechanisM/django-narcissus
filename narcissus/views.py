from django.views.generic import TemplateView

from narcissus.settings import STATIC_URL


class HomeView(TemplateView):
    template_name = "narcissus/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'NARCISSUS_STATIC_URL': STATIC_URL,
        })
        return context
