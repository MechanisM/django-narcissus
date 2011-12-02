from django.conf.urls.defaults import patterns, include, url

from narcissus.dashboard.views import HomeView, PostCreateView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='narcissus-home'),
    url(r'^new/([\w-]+)/$', PostCreateView.as_view(),
        name='narcissus-new-post'),
)
