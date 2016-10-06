from django import forms
from django.contrib.auth.forms import UserCreationForm

class SubscriberForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

# class SearchForm(forms.ModelForm):
# 	search_query = forms.CharField(max_length=100)