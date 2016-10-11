from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Contact
from .forms import ContactForm

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
def contact_cru(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
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
		form = ContactForm()
		
	variables = {'form': form}
	template = 'contacts/contact_cru.html'
	return render(request, template, variables)
>>>>>>> hedit
