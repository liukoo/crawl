from django.conf.urls.defaults import *
from crawl.views import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crawl.views.home', name='home'),
    # url(r'^crawl/', include('crawl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^index/$', include(index)),
     url(r'^static/.*$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS},name='static'),
     url(r"^add_task/?$",add_task,name='add_task'),
     url('^.*$', index),
)
