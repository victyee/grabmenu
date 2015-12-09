from django.db import models

# Create your models here.


class ContactUs(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=120)
	contact_number = models.CharField(max_length=100, null=True, blank=True)
	subject = models.CharField(max_length=120, null=True, blank=True)
	message = models.TextField(max_length=850)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.name