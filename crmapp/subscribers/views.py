from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.urlresolvers import reverse

from .forms import SubscriberForm
from .models import Subscriber

import stripe

# Create your views here.
def subscriber_new(request, template='subscribers/subscriber_new.html'):
	if request.method == 'POST':
		form = SubscriberForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			
			# Create the user record
			user = User(username=username, email=email,
						first_name=first_name, last_name=last_name)
			user.set_password(password)
			user.save()

			# Create the subscriber record
			address_one = form.cleaned_data['address_one']
			address_two = form.cleaned_data['address_two']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			sub = Subscriber(address_one=address_one, address_two=address_two,
								city=city, state=state)
			sub.save()
			# Process payment (via Stripe)
			fee = settings.SUBSCRIPTION_PRICE
			try:
				stripe_customer = sub.charge(request, email, fee)
			except stripe.StripeError as e:
				form._errors[NON_FIELD_ERRORS] = form.error_class([e.args[0]])
				return render(request, template,
					{'form':form,
					'STRIPE_PUBLISHABLE_KEY':settings.STRIPE_PUBLISHABLE_KEY}
					)

			# Auto login the user
			a_u = authenticate(username=username, password=password)
			if a_u is not None:
				if a_u.is_active:
					login(request, a_u)
					return HttpResponseRedirect(reverse('account_list'))

				else:
					return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))

			else:
				return HttpResponseRedirect(reverse('sub_new'))

			return HttpResponseRedirect('/success/')
	else:
		form = SubscriberForm()
		
	return render(request, template,
		{'form':form, 
		'STRIPE_PUBLISHABLE_KEY':settings.STRIPE_PUBLISHABLE_KEY})

# def search(request):
# 	if request.methods == 'POST':
# 		form = SeachForm(request.POST)
# 		if form.is_valid():
# 			s_query = form.cleaned_data['search_query']
# 			s_result = SomeTable.objects.filter(name=s_query)			
# 			return render(request, 'search_form.html', {'form': form, 's_query': s_query})
# 	else:
# 		form = SeachForm()
# 	return render(request, 'search_form.html', {'form': form})
