from django.contrib import admin

# Register your models here.

from .models import OwnersSubmit

class OwnersSubmitAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp"]
	class Meta:
		model = OwnersSubmit

admin.site.register(OwnersSubmit, OwnersSubmitAdmin)