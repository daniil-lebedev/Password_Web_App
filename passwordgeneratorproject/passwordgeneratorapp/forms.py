from django.forms import ModelForm, IntegerField, CharField
from .models import *
from django import forms


"""Form for creating new passwords"""
class PasswordForm(ModelForm):
	class Meta:
		model = Password
		fields = '__all__'

"""Form to generate passowrds"""
class PasswordGeneratorForm(forms.Form):
	lower_case_letters_amount = IntegerField()
	upper_case_letters_amount = IntegerField()
	numbers_amount = IntegerField()

"""Form to check passowrds"""
class PasswordChecker(forms.Form):
	checkingpassword = CharField()	

"""Form to generate a new credit card"""
class CreditCardForm(ModelForm):
	class Meta:
		model = CreditCard
		fields = ['name','cardNumber','date','securityCode']
		
			