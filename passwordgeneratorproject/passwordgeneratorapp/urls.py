from django.urls import path
from . import views
from passwordgeneratorapp.views import GeneratePasswordView, CheckPassword, creditCard


urlpatterns = [
	#path for initial stuff
    path('', views.index, name="index"),
    path('add', views.add, name='add'),

    #path for password creation and check
    path('delete/<password_id>', views.passwordDelete, name="delete"),
    path('passwordgenerator', GeneratePasswordView.as_view(), name="passwordgenerator"),
    path('passwordchecker', CheckPassword.as_view(), name='passwordchecker'),

    #path for creadit card details
    path('credit-card-form', views.creditCard, name="creditCardFormPage"),
    path('credit-card-display', views.creaditCardView, name="CreditCardDisplayPage"),

    #path for register page
    path('register', views.createuser, name="register")
]