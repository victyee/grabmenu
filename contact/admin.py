from django.contrib import admin

# Register your models here.

from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "email", "subject", "timestamp"]
	class Meta:
		model = ContactUs

admin.site.register(ContactUs, ContactUsAdmin)