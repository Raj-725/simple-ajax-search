from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	# demo urls
    url(r'^$', 'demo.views.home', name='home'),
    url(r'^search/$', 'demo.views.search', name='search'),

    # admin urls:
    url(r'^admin/', include(admin.site.urls)),
)
