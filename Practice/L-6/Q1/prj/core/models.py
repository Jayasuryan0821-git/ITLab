from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    english = models.IntegerField()
    chemistry = models.IntegerField()
    physics = models.IntegerField()