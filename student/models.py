from django.db import models

# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    added_at= models.DateTimeField(auto_now_add=True)
    submission_date = models.DateField()