from django.conf.urls.defaults import patterns, include, url

from narcissus.garden.views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='narcissus-home'),
)
