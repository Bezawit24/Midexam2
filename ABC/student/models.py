from django.db import models
class students(models.Model):
       fname=models.CharField(max_length=100)
       lname=models.CharField(max_length=100)
       grade=models.CharField(max_length=2)
       def __str__(self):
            return self.fname
       
class empolyee(models.Model):
       fname=models.CharField(max_length=100)
       lname=models.CharField(max_length=100)
       salary=models.CharField(max_length=2)
       def __str__(self):
            return self.fname      
         
class teachers(models.Model):
       fname=models.CharField(max_length=100)
       lname=models.CharField(max_length=100)
       salary=models.CharField(max_length=2)
       def __str__(self):
            return self.fname

# Create your models here.
