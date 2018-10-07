from django import forms
from .models import imagen

class ImagenForm(forms.ModelForm):
	class Meta:
		model = imagen
		fields = ['foto']