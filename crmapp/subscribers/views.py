from django.shortcuts import render
from subscribers.forms import SeachForm

# Create your views here.

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
