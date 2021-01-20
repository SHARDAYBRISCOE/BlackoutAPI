from django.db import models

# Create your models here.
class Employee(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	emp_id = models.IntegerField()

	def __str__(self):
		return self.firstname 

class Business(models.Model):
	business_name = models.CharField(max_length=1000)
	website = models.CharField(max_length=1000)

	def __str__(self):
		return self.business_name