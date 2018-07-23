from django.db import models

# Create your models here.
class Company(models.Model):
	company_name = models.CharField(max_length=100)
	company_address = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	contactno = models.CharField(max_length=10)

	def __str__(self):
		return self.company_name

	
class Job(models.Model):
	company = models.ForeignKey(
		Company,
		on_delete=models.CASCADE,
		related_name = 'job'
	)
	designation = models.CharField(max_length=100)
	hr_name = models.CharField(max_length=100)
	experience = models.CharField(max_length=10)
	vacancy = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	salary = models.CharField(max_length=100)
	jobtype = models.CharField(max_length=100)
	required_skills = models.CharField(max_length=1000)

	def __str__(self):
		return self.designation

	class Meta:
		ordering = ('designation',)

class Seeker(models.Model):
	s_name = models.CharField(max_length=20,null=False,blank=False)
	jobs =  models.ManyToManyField(Job)
	email = models.EmailField(max_length=100)
	contactno = models.CharField(max_length=10)
	skills = models.CharField(max_length=100)

	def __str__(self):
		return self.s_name

	class Meta:
		ordering = ('s_name',)

