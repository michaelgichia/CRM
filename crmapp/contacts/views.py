from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.HttpResponseForbidden

from .models import Contact
from crmapp.accounts.models import Account

# Create your views here.
@login_required()
def account_detail(request, uuid):
	account = Account.objects.get(uuid=uuid)

	if account.owner != request.user:
		return HttpResponseForbidden()
	contact = Contact.objects.filter(account=account)

	variables = {
				'account': account,
				'contact': contact,}

	return render(request, 'contacts/contact_detail.html', variables)