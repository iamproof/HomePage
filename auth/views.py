from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from auth.models import RegNumber
import random
from django.contrib import messages


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ( "username", "email","first_name", "last_name", "password1", "password2" )

class ValidateForm(forms.Form):
	user = forms.CharField(max_length=30)
	validate_number = forms.FloatField()


def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('auth:logged_in')
				else:
					# Return a 'disabled account' error messag
					return redirect('auth:disabled')
			else:
				return redirect('auth:invalid')
	else:
		form = LoginForm()

	return render(request, 'auth/index.html', {'form': form})


def logged_out(request):
	logout(request)
	return render_to_response('auth/logged_out.html')

def logged_in(request):
	return render(request, 'auth/logged_in.html', {'name': request.user.username})

def invalid(request):
	return render_to_response('auth/invalid.html')

def disabled(request):
	return render_to_response('auth/disabled.html')


def registration(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			who = form.cleaned_data['username']
			user = User.objects.get(username=who)
			user.is_active = False

			email = form.cleaned_data['email']
			number = random.random()
			try:
				regnumber = RegNumber.objects.create(user=who, number=number)
				regnumber.save()
			except:
				return render(request, 'auth/registration.html', {'form': RegistrationForm(), 'info': 'This user is not available.'})
			user.save()	

			send_mail('Django registration confirmation', 'Please visit http://jacek-karnasiewicz.rhcloud.com/auth/confirmation/ and here is the confirmation number {}'.format(number), 'karnasiewicz.jacek@gmail.com',
    				 [email], fail_silently=False)
			return redirect('auth:confirmation')
		else:			
			return render(request, 'auth/registration.html', {'form': RegistrationForm(), 'info': 'Invalid Data !'})
	else:
		form = RegistrationForm()
		return render(request, 'auth/registration.html', {'form': form})

def confirmation(request):
	if request.method == "POST":
		form = ValidateForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data['user']
			validate_number = form.cleaned_data['validate_number']
			try:
				if validate_number == RegNumber.objects.get(user=user).number:
					validate_user = User.objects.get(username=user)
					validate_user.is_active = True
					validate_user.save()
					# And we delete our RegNumber
					RegNumber.objects.get(user=user).delete()
					messages.info(request, 'Now you are active user!')
					return redirect("auth:index")
			except:
				messages.info(request, 'Invalid Data!')
				return redirect("auth:confirmation")
			else:
				messages.info(request, 'Invalid Data!')
				return redirect("auth:confirmation")
		else:
			messages.info(request, 'Invalid Form Values!')
			return redirect("auth:confirmation")

	return render(request, 'auth/confirmation.html', {'form': ValidateForm()})




