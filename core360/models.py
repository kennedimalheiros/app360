from django.db import models
from django import forms

# Create your models here.
class Office(models.Model):
	name = models.CharField(max_length=100)
	level = models.IntegerField()

	def __unicode__(self):
		return self.name

class Department(models.Model):
	description = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.description + ' - ' + self.phone

class Employee(models.Model):
	name = models.CharField(max_length=100)
	boss = models.IntegerField()
	department = models.ForeignKey(Department)
	office = models.ForeignKey(Office)
	user = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

