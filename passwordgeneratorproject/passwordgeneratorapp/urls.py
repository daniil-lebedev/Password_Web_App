from django.urls import path
from . import views
from passwordgeneratorapp.views import GeneratePasswordView, CheckPassword


urlpatterns = [
	#path for initial stuff
    path('', views.index, name="index"),
    path('add', views.add, name='add'),

    #path for password creation and check
    path('delete/<password_id>', views.passwordDelete, name="delete"),
    path('passwordgenerator', GeneratePasswordView.as_view(), name="passwordgenerator"),
    path('passwordchecker', CheckPassword.as_view(), name='passwordchecker'),

    #path for register page
    path('register', views.createuser, name="register")
]