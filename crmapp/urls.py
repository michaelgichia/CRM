from django.conf.urls import patterns, include, url
from django.contrib import admin

from marketing.views import Homepage

urlpatterns = patterns('',

	# Market pages url.
	
	url(r'^$', Homepage.as_view(), name='home'),
    # Examples:
    # url(r'^$', 'crmapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
