from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    marks_english = models.IntegerField()
    marks_physics = models.IntegerField()
    marks_chemistry = models.IntegerField()

