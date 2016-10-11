from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .models.communications import Communication

# Create your views here.
@login_required()
def comm_detail(request, uuid):

	comm = Communication.objects.get(uuid=uuid)
	if comm.owner != request.user:
		return HttpResponseForbidden()

	template = 'communications/comm_details.html'
	variables = {'comm': comm}
	return render(request, template, variables)