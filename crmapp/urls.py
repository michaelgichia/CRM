from django.conf.urls import patterns, include, url
from django.contrib import admin

from accounts.urls import account_urls
from contacts.urls import contact_urls

from marketing.views import Homepage
from accounts.views import AccountList


admin.autodiscover()

urlpatterns = patterns('',

	# Market pages url.
	
	url(r'^$', Homepage.as_view(), name='home'),
    url(r'^acount/new/$', 'crmapp.accounts.views.account_cru', name='account_new'),
	url(r'^signup/$', 'crmapp.subscribers.views.subscriber_new', name='sub_new'),
    # Examples:
    # url(r'^$', 'crmapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Login/Logout URLs
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
    url(r'^account/list/$', AccountList.as_view(), name='account_list'),
    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
    url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),
    url(r'^contact/new/$', 'crmapp.contact.views.contact_cru', name='contact_new')


)
