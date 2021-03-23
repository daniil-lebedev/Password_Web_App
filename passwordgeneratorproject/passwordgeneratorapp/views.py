from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Password
from .forms import PasswordForm, PasswordGeneratorForm
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
			text = form.cleaned_data['post']
			#I want to load the form but also pass text
		args = {'form':form, 'text':text}
		return render(request, self.template_name, args)