from django.conf.urls.defaults import patterns, include, url

from narcissus.dashboard.views import HomeView, PostCreateView, PostDeleteView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='narcissus-home'),
    url(r'^new/(?P<posttype_name>[\w-]+)/$', PostCreateView.as_view(),
        name='narcissus-new-post'),
    url(r'^delete/(?P<posttype_name>[\w-]+)/(?P<pk>\d+)/$',
        PostDeleteView.as_view(), name='narcissus-delete-post'),
)
