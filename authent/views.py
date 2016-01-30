from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.models import User
import json
# Create your views here.

def index(request):

	if request.user.is_authenticated():
		return redirect('/forum')
	else:
		return redirect('/authent/signin')

def signout(request):
	#print "logging out" this also clears all session data
	logout(request) 
	return redirect('/authent/')


def signin(request):
	if request.user.is_authenticated() == True:
		return redirect('/forum')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is None:
			return render(request,'signin.html',{'error':'Invalid username or password'})

		else:
			login(request,user)
			return redirect('/forum/') #render the forum page
	else:
		return render(request,'signin.html',None)

def signup(request):
	if request.user.is_authenticated() == True:
		return redirect('/forum')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password2 = request.POST['password2']
		firstName = request.POST['firstName']
		lastName = request.POST['lastName']
		if password2 != password:
			return render(request,'signup.html',{'error':'Password doesn\'t match'}) 

		emailAddr = request.POST['email']

		try:
			u = User._default_manager.get(username__iexact=username) #fix for case sensitive username
			return render(request,'signup.html',{'error':'username already already exists!'})
		except User.DoesNotExist:
			user = User.objects.create_user(username=username,email=emailAddr,first_name=firstName,last_name=lastName)
			user.set_password(password)
			user.save()
			user.backend = 'django.contrib.authent.backends.ModelBackend' #user backend error fix
			authenticate(username=username,password=password)
			login(request,user)
			return redirect('/forum/')
	else:
		return render(request,'signup.html',None)
