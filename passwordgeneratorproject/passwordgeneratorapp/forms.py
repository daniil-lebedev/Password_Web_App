from django.forms import ModelForm
from .models import *

"""Form for creating new passwords"""
class PasswordForm(ModelForm):
	class Meta:
		model = Password
		fields = '__all__'