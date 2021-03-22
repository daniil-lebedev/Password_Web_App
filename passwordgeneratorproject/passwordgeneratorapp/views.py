from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Password
from .forms import PasswordForm

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