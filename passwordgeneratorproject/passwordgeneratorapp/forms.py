from django.forms import ModelForm
from .models import *
from django import forms

"""Form for creating new passwords"""
class PasswordForm(ModelForm):
	class Meta:
		model = Password
		fields = '__all__'

class PasswordGeneratorForm(forms.Form):
	post = forms.CharField()