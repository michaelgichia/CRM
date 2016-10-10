from django.conf.urls import patterns, url


contact_urls = patterns('',
	url(r'^$', 'crmapp.contact.views.contact_detail', name='contact_detail'),
	)