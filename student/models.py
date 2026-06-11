from django.db import models

# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    added_at= models.DateTimeField(auto_now_add=True)
    submission_date = models.DateField()
    
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    added_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100)

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    address = models.CharField(max_length=500)
    email=models.EmailField()
    picture=models.ImageField(upload_to='teacherdp')
    department = models.CharField(max_length=100)