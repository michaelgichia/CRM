from django.shortcuts import render
from django.generic.views import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Account


# Create your views here.
class AccountList(ListView):
	model = Account
	paginate_by = 12
	template_name = 'accounts/account_list.html'
	context_object_name = 'account'

	def query_set(self):
		account_list = Account.objects.filter(owner=self.request.user)
		return account_list

	@method_decorator(login_required)
	def dispatch(self, *agrs, **kwargs):
		super(AccountList, self).dispatch(*agrs, **kwargs)
