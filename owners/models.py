from django.db import models
from django.db.models.signals import post_save
from django.conf import settings

class OwnersSubmit(models.Model):
	#restaurant details
	restaurant_name = models.CharField(max_length=200)
	street_address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=50)
	menu = models.FileField(upload_to='restaurant/menu/', null=True, blank=True)
	website = models.CharField(max_length=350, null=True, blank=True)

	#owner's details
	owner_name = models.CharField(max_length=150)
	contact_number = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	message = models.TextField(max_length=1000, null=True, blank=True)

	def __unicode__(self):
		return self.restaurant_name