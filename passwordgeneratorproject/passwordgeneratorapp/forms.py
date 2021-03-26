from django.forms import ModelForm, IntegerField, CharField
from .models import *
from django import forms


"""Form for creating new passwords"""
class PasswordForm(ModelForm):
	class Meta:
		model = Password
		fields = '__all__'

class PasswordGeneratorForm(forms.Form):
	lower_case_letters_amount = IntegerField()
	upper_case_letters_amount = IntegerField()
	numbers_amount = IntegerField()

class PasswordChecker(forms.Form):
	checkingpassword = CharField()	
		