from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, default =1, on_delete = models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	CHOICES = (
		('FEMALE', 'female'),
		('MALE', 'male')
		)

	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=6, choices = CHOICES, default = 'FEMALE')
	exam_grade = models.DecimalField(max_digits=6, decimal_places=3 )
	classroom = models.ForeignKey(Classroom, default =1, on_delete = models.CASCADE)
