from django.conf.urls.defaults import patterns, include, url

from narcissus.garden.views import HomeView, PetalCreateView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='narcissus-home'),
    url(r'^new/([\w-]+)/$', PetalCreateView.as_view(),
        name='narcissus-new-petal'),
)
