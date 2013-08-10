from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Blog detail url
    url(r'^(?P<blog_slug>.+)/(?P<slug>.+)/$', 'schick.blog.views.blog_detail', name='blog_detail'),

    # Blog index URL
    url(r'^(?P<blog_slug>.+)/$', 'schick.blog.views.blog_index', name='blog_index'),    
)