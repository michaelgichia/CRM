from django.conf.urls import patterns, include, url
from django.contrib import admin

from marketing.views import Homepage

admin.autodiscover()

urlpatterns = patterns('',

	# Market pages url.
	
	url(r'^$', Homepage.as_view(), name='home'),
	url(r'^signup/$', 'crmapp.subscribers.views.subscriber_new', name='sub_new'),
    # Examples:
    # url(r'^$', 'crmapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
