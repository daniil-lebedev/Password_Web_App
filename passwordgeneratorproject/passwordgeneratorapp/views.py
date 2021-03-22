from django.shortcuts import render
from .models import Password

# Create your views here.
def index(request):
    all_passwords = Password.objects.all()
    return render(request, 'index.html', 
    {'all_passwords': all_passwords})