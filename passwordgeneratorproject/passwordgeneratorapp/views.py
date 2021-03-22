from django.shortcuts import render
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
	return render(request, 'add.html',
		{'form':PasswordForm})
