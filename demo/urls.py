from django.conf.urls.defaults import *
from demo.views import *

urlpatterns = patterns( '',
	url( r'^$', index, name = 'index' ),
	url( r'^users/$', search, name = 'search' ),
) 
