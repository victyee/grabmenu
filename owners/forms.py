from django import forms

from .models import OwnersSubmit

class OwnersSubmitForm(forms.ModelForm):
	class Meta:
		model = OwnersSubmit
		fields = ["restaurant_name",
				"street_address",
				"city",
				"state",
				"menu",
				"website",
				"owner_name",
				"contact_number",
				"email",
				"message",
				]

