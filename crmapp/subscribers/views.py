from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import SubscriberForm
from .models import Subscriber

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
			return HttpResponseRedirect('/success/')
	else:
		form = SubscriberForm()
		return render(request, template, {'form': form})


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
