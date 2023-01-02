from django.db import models

# Create your models here.
class teachers(models.Model):
       fname=models.CharField(max_length=100)
       lname=models.CharField(max_length=100)
       salary=models.CharField(max_length=2)
       def __str__(self):
            return self.fname
