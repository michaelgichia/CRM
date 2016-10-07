from django.conf.urls import patterns, include, url
from django.contrib import admin

from marketing.views import Homepage
from accounts.views import AccountList

admin.autodiscover()

urlpatterns = patterns('',

	# Market pages url.
	
	url(r'^$', Homepage.as_view(), name='home'),
	url(r'^signup/$', 'crmapp.subscribers.views.subscriber_new', name='sub_new'),
    # Examples:
    # url(r'^$', 'crmapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Login/Logout URLs
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
    url(r'^account/list/$', AccountList.as_view(), name='account_list'),
)
