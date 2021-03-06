from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .forms import CommunicationForm 
from .models import Communication

# Create your views here.
@login_required()
def comm_detail(request, uuid):

	comm = Communication.objects.get(uuid=uuid)
	if comm.owner != request.user:
		return HttpResponseForbidden()

	template = 'communications/comm_details.html'
	variables = {'comm': comm}
	return render(request, template, variables)

 


@login_required()
def comm_cru(request):

	if request.POST:
		form = CommunicationForm(request.POST)

	if form.is_valid():
		# make sure the user owns the account
		account = form.cleaned_data['account']
		if account.owner != request.user:
			return HttpResponseForbidden()
		# save the data
		comm = form.save(commit=False)
		comm.owner = request.user
		comm.save()
		# return the user to the account detail view
		reverse_url = reverse(
		'crmapp.accounts.views.account_detail',
		args=(account.uuid,)
		)
		return HttpResponseRedirect(reverse_url)
	else:
		form = CommunicationForm()

	variables = {
		'form': form,
		}

	template = 'communications/comm_cru.html'

	return render(request, template, variables)
