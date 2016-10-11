from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Contact
from .forms import ContactForm
from crmapp.accounts.models import Account 

# Create your views here.
@login_required()
def contact_detail(request, uuid):
	
	contact = Contact.objects.get(uuid=uuid)

<<<<<<< HEAD
	return render(request, 
		'contacts/contact_detail.html', 
		{'contact': contact})
=======
	return render(request, 'contacts/contact_detail.html', {'contact': contact})

@login_required()
def contact_cru(request, uuid=None, account=None):

	if uuid:
		contact = get_object_or_404(Contact, uuid=uuid)
		if contact.owner != request.user:
			return HttpResponseForbidden()
	else:
		contact = Contact(owner=request.user)

	if request.method == 'POST':
		form = ContactForm(request.POST, instance=contact)
		if form.is_valid():
			account = form.cleaned_data['account']
			if account.owner != request.user:
				return HttpResponseForbidden()

			contact = form.save(commit=False)
			contact.owner = request.user
			contact.save()

			reverse_url = reverse('crmapp.accounts.views.account_detail', agrs=(account.uuid))
			return HttpResponseRedirect(reverse_url)
		else:
			account = form.cleaned_data['account']

	else:
		form = ContactForm(instance=contact)
	
	if request.GET.get('account', ''):
		account = Account.objects.get(id=request.GET.get('account', ''))

	variables = {
		'form': form,
		'contact': contact,
		'account': account
		}

	template = 'contacts/contact_cru.html'
<<<<<<< HEAD
	return render(request, template, variables)
>>>>>>> hedit
=======
		
	return render(request, template, variables)
>>>>>>> medit
