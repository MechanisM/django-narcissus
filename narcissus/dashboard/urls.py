from django.conf.urls.defaults import patterns, include, url

from narcissus.dashboard.views import HomeView, PostCreateView, PostDeleteView
from narcissus.settings import STATIC_URL


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='narcissus-home'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        kwargs={'template_name': 'narcissus/dashboard/login.html',
                'extra_context': {'NARCISSUS_STATIC_URL': STATIC_URL}},
        name='narcissus-login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        kwargs={'template_name': 'narcissus/dashboard/logged_out.html',
                'extra_context': {'NARCISSUS_STATIC_URL': STATIC_URL}},
        name='narcissus-logout'),
    url(r'^new/(?P<posttype_name>[\w-]+)/$', PostCreateView.as_view(),
        name='narcissus-new-post'),
    url(r'^delete/(?P<posttype_name>[\w-]+)/(?P<pk>\d+)/$',
        PostDeleteView.as_view(), name='narcissus-delete-post'),
)
