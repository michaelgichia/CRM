from django import forms

from .models import Account

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ('name', 'desc', 'address_one', 'address_two', 'city', 'state', 'phone')
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Company', 'class': 'col-md-12 form-class'}),
			'desc': forms.TextInput(attrs={'placeholder': 'Enter a description', 'class': 'form-class'}),
			'address_one': forms.TextInput(attrs={'placeholder': 'Street Address', 'class': 'gi-form-addr form-class'}),
			'address_two': forms.TextInput(attrs={'placeholder': 'Suite, PO, etc', 'class': 'gi-form-addr form-class'}),
			'city': forms.TextInput(attrs={'placeholder': 'City', 'class': 'gi-form-addr form-class'}),
			'state': forms.TextInput(attrs={'placeholder': 'State', 'class': 'gi-form-addr form-class'}),
			'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'gi-form-addr form-class'}),

		}