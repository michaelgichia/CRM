from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import SubscriberForm

# Create your views here.
def subscriber_new(request, template='subscribers/subscriber_new.html'):
	if request.method == 'POST':
		form = SubscriberForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			# Create the user record
			user = User(username=username, email=email)
			user.set_password(password)
			user.save()
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
