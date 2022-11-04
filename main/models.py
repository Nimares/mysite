from django.db import models

# Create your models here.
class Car(models.Model):
    STATUS_TYPE=(('available','available'),('booked','booked'),('rented','rented'),('damaged','damaged'))
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year=models.IntegerField(null=True)
    location=models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=10, choices=STATUS_TYPE, null=True)

class Customer(models.Model):
     name = models.CharField(max_length=50)
     address = models.CharField(max_length=50)
     age= models.IntegerField()

     def __str__(self): 
       return self.name+' '+self.address+' '+self.age

class Employee(models.Model):
     name = models.CharField(max_length=50)
     address = models.CharField(max_length=50)
     branch=models.CharField(max_length=50)

     def __str__(self): 
       return self.name+' '+self.address+' '+self.branch
    
