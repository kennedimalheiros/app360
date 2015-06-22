from django.db import models

# Create your models here.
class Cargo(models.Model):
	name = models.CharField(max_length=100)
	level = models.IntegerField()

	def __unicode__(self):
		return self.name
