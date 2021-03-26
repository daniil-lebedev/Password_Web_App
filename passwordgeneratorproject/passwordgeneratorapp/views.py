from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Password
from .forms import PasswordForm, PasswordGeneratorForm, PasswordChecker
import random
import string
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    all_passwords = Password.objects.all()
    return render(request, 'index.html', 
    {'all_passwords': all_passwords})

def add(request):
	if request.method == "POST":
		form = PasswordForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('index')
	return render(request, 'add.html',
		{'form':PasswordForm})

def passwordDelete(request,password_id):
	item = Password.objects.get(pk=password_id)
	item.delete()
	return redirect('index')

class GeneratePasswordView(TemplateView):
	template_name = 'passwordgenerator.html'

	def get(self, request):
		form = PasswordGeneratorForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = PasswordGeneratorForm(request.POST)
		if form.is_valid():
			#getting the result of that post request and making sure that nothing dangerous is sumbitted
			amount_of_low_let = form.cleaned_data['lower_case_letters_amount']
			amount_of_up_let = form.cleaned_data['upper_case_letters_amount']
			amount_of_numbers = form.cleaned_data['numbers_amount']
			
			#generate characters for passowrds
			letters_low = string.ascii_lowercase
			letters_up = string.ascii_uppercase
			var_list = []
			password_list = []
			password_list.append(random.choice(letters_up))

			#generate values for numbers
			for i in range(0,amount_of_numbers):
				if amount_of_numbers == 0:
					pass
				var_list.append(random.randrange(10))

			#generate value for lowercase letters
			for y in range(0, amount_of_low_let):
				if amount_of_low_let == 0:
					pass
				var_list.append(random.choice(letters_low))

			#generate value for uppercase letters
			for x in range(0, amount_of_up_let):
				if amount_of_up_let == 0:
					pass
				var_list.append(random.choice(letters_up))

			#putting all the stuff together
			password_list.extend(var_list)
			random.shuffle(password_list)
			password_list = [str(int) for int in password_list]
			password_list = "".join(password_list)
			password_list = str(password_list)
			

		args = {'form':form, 'password_list':password_list }
		return render(request, self.template_name, args)

"""Class to check the password"""
class CheckPassword(TemplateView):
	template_name = 'passwordcheck.html'

	def get(self,request):
		form = PasswordChecker(request.POST)
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		args = {'form':form}
		return render(request, self.template_name,args)