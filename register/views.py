from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import profileform
from register.models import profile
# Create your views here.register views


#login block
def login(request):
	if request.user.is_authenticated:
		return redirect('home')
		
	if(request.method=='POST'):
		username=request.POST.get('username').lower()
		password=request.POST.get('password')
		#print(username,password)
		user=authenticate(username=username,password=password)
		
		if user is not None:
			#set username in session
			request.session['username']=username
			auth.login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Enter valid username or password')
			return redirect('/')
		
	return render(request,'login.html')
#end login block	
	
#register block	
def register(request):
	if(request.method=='POST'):
		username=request.POST.get('username').lower()
		email=request.POST.get('email').lower()
		password=request.POST.get('password')
		cpassword=request.POST.get('cpassword')
		#print(username,email,password,cpassword)
		if password==cpassword:
			if User.objects.filter(username=username).exists():
				messages.info(request,'User Exists')
				return redirect('register')
			
			if User.objects.filter(email=email).exists():
				messages.info(request,'Email Exists')
				return redirect('register')
				
			user=User.objects.create_user(username,email,password)
			user.save()
			return redirect('/')
		
		else:
			messages.info(request,'Password Not Match')
			return redirect('register')
			
	return render(request,'register.html')
#end register block

#home
def home(request):
	if request.user.is_authenticated:
		return render(request,'home.html')
	#if request.session.has_key('username'):
		#return render(request,'home.html')
	return redirect('/')
#endhome

#logout
def logout(request):
	if request.user.is_authenticated:
		#print(request.session.get('username'))
		del request.session['username']
		#print(request.session.get('username'))
		auth.logout(request)
	return redirect('/')	
#endlogout

#profile
def profilefun(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			suser=request.session.get('username')
			data=User.objects.get(username=suser)
			username=request.POST.get('username').lower()
			email=request.POST.get('email').lower()
			#print(username,email)
			if username==data.username:
				pass
			else:
				if User.objects.filter(username=username).exists():
					messages.info(request,'user exists')
					return redirect('profile')
				data.username=username
				data.save()
				#request.session['username']=data.username
				
			if email==data.email:
				pass
			else:
				if User.objects.filter(email=email).exists():
					messages.info(request,'email exists')
					return redirect('profile')
				data.email=email
				data.save()
				
			try:
				fd=profile.objects.get(username=suser)
				form=profileform(request.POST,request.FILES,instance=fd)
				if form.is_valid():
					request.session['username']=data.username
					ofd=form.save(commit=False)
					ofd.username=data.username
					ofd.user=data
					ofd.save()
			except Exception as e:
				form=profileform(request.POST,request.FILES)
				if form.is_valid():
					request.session['username']=data.username
					ofd=form.save(commit=False)
					ofd.username=data.username
					ofd.user=data
					ofd.save()
			
		#upside post request code
		
		suser=request.session.get('username')
		try:
			fd=profile.objects.get(username=suser)
			form=profileform(instance=fd)
		except Exception as e:
			form=profileform()
			
		data=User.objects.get(username=suser)
		return render(request,'profile.html',{'form':form,'data':data})
			
	return redirect('/')
#profileend
