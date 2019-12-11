from django.db import models

# Create your models here.

class Appointment(models.Model):
    patient_name=models.CharField(max_length=25,default="")
    patient_number=models.CharField(max_length=15,default="")
    problem_detail=models.CharField(max_length=200,default="")

class Feedback(models.Model):
    name=models.CharField(max_length=20,default="")
    contact=models.CharField(max_length=15,default="")
    feedback=models.CharField(max_length=200,default="")

