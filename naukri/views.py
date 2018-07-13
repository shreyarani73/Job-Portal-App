from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from .forms import *
# Create your views here.
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
	return HttpResponse('<h1>done</h1>')
	# if request.method == 'POST':
	# 	newcomp = Company.objects.create(
	# 			company_name = request.POST['company_name'],
	# 			company_address = request.POST['company_address'],
	# 			description = request.POST['description'],
	# 			contactno = request.POST['contactno'],

	# 	newcomp.save()
	# 	context = {'newcomp': newcomp}
	# else:
	# 	context = {}
	# return render(request, 'naukri/addnewcompany.html',context)

