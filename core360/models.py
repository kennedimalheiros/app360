#coding:utf-8
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Office(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Department(models.Model):
	description = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.description + ' - ' + self.phone

class Employee(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=100)
	boss = models.ForeignKey( 'self', null=True, blank=True, help_text='Responsável', related_name='employee_boss' )
	department = models.ForeignKey(Department)
	office = models.ForeignKey(Office)
	
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Funcionário'
		verbose_name_plural = 'Funcionários'

class Quiz(models.Model):
	
	title = models.CharField(max_length=40)	
	registration_date = models.DateField(blank=False)	
	employee = models.ManyToManyField(Employee, related_name='Avaliado')
	description_of_work = models.TextField(max_length=500, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Questionário'
		verbose_name_plural = 'Questionários'

class Evaluation(models.Model):
	employee_assessed = models.ForeignKey(Employee)
	person_will_answer_form = models.ForeignKey(Employee, related_name = 'avaliador')
	registration_date = models.DateField()	
	quiz  = models.ForeignKey(Quiz)
	

	class Meta:
		verbose_name = 'Avaliação'
		verbose_name_plural = 'Avaliações'

class Options(models.Model):
	text = models.CharField(max_length=100)

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Opçao'
		verbose_name_plural = 'Opções'

class Question(models.Model):
	text = models.CharField(max_length=500)
	quiz = models.ManyToManyField(Quiz)
	options = models.ManyToManyField(Options)	

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Questão'
		verbose_name_plural = 'Questões'
