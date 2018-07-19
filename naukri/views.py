from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.template import RequestContext
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
# Create your views here.

# this login required decorator is to not allow to any  
# view without authenticating

def mylogin(request):
	msg=[]
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				msg.append("login successful")
				return HttpResponseRedirect('/')
			else:
				msg.append("disabled account")
		else:
			msg.append('invalid username/password')
	else:
		msg.append('Invalid Login')
	return render(request,'naukri/login.html', {'errors': msg})

# this login required decorator is to not allow to any  
# view without authenticating
# @login_required(login_url="login/")


def mylogout(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')

def index(request):
	alljob = Job.objects.all()
	return render(request, 'naukri/index.html', {'alljob':alljob})

def jobdetail(request,job_id):
	detail = Job.objects.get(pk = job_id)
	return render(request, 'naukri/jobdetail.html', {'detail':detail})

def apply(request, job_id):
	if request.method == 'POST':
		applicant = Seeker.objects.create(
			s_name = request.POST['s_name'],
			email = request.POST['email'],
			contactno = request.POST['contactno'],
			skills = request.POST['skills'])
		applicant.save()
		context = {'applicant':applicant}
	else:
		context = {}
	return render(request, 'naukri/newuser.html',context)

def addnewjob(request):
	# return HttpResponse('<h1>adding</h1>')
	if request.method == 'POST':
		newjob = Job.objects.create(
			designation = request.POST['designation'],
			hr_name = request.POST['hr_name'],
			experience = request.POST['experience'],
			vacancy = request.POST['vacancy'],
			place = request.POST['place'],
			salary = request.POST['salary'],
			jobtype = request.POST['jobtype'],
			required_skills = request.POST['required_skills'])
		applicant.save()
		context = {'newjob':newjob}
	else:
		context = {}
	return render(request, 'naukri/addnewjob.html',context)

def addnewcompany(request):
	if request.method == 'POST':
		newcomp = Company.objects.create(
			company_name = request.POST['company_name'],
			company_address = request.POST['company_address'],
			description = request.POST['description'],
			contactno = request.POST['contactno'])
		newcomp.save()
		context = {'newcomp':newcomp}
	else:
		context = {}
	return render(request,'naukri/addnewcompany.html',context)