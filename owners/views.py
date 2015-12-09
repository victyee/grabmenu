import re

from django.shortcuts import render, HttpResponseRedirect
from django import forms
from django.contrib import messages
from django.conf import settings
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .forms import OwnersSubmitForm
from .models import OwnersSubmit

# Create your views here.

def owners(request):
	if request.method == 'GET':
		owners_submit_form = OwnersSubmitForm(request.POST, request.FILES)
		context = {
			'owners_submit_form': owners_submit_form
			}
		return render(request, 'owners/owners.html', context)

	elif request.method == "POST":
		restaurant_name = request.POST.get('restaurant_name', '')
		street_address = request.POST.get('street_address', '')
		city = request.POST.get('city', '')
		state = request.POST.get('state', '')

		menu = request.POST.get('menu', '')
		website = request.POST.get('website', '')

		owner_name = request.POST.get('owner_name', '')
		contact_number = request.POST.get('contact_number', '')
		email = request.POST.get('email', '')
		message = request.POST.get('message', '')

		owners_submit_form = OwnersSubmitForm(request.POST, request.FILES)
		context = {
			'owners_submit_form': owners_submit_form,
			'restaurant_name': restaurant_name,
			'street_address': street_address,
			'city': city,
			'state': state,
			'menu': menu,
			'website': website,
			'owner_name': owner_name,
			'contact_number': contact_number,
			'email': email,
			'message': message,
			}

		if owners_submit_form.is_valid():
			new_query = owners_submit_form.save()
			new_query.save()
			messages.success(request, "Thank you, your request has been successfully sent. We'll get back to you soon.")
			return HttpResponseRedirect("/")
		else:
			messages.error(request, "* fields are required.")
	return render(request, 'owners/owners.html', context)
