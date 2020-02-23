from django.db import models

# Create your models here.
'''
models.py is used to identify all tables in a database
it is used to specify the attributes of a table and the relationship's between each of the tables if any
'''
class owner(models.Model):
    name=models.CharField(max_length=30,default="none")#name of owner
    email=models.EmailField(max_length=30,default="none")#email of owner
    ph=models.CharField(max_length=10,default="none")#mobile number of owner
    address=models.CharField(max_length=100,default="none")#address of owner
class pet(models.Model):
    name=models.CharField(max_length=30,default="none")#this is used to store the name of the pet
    owner=models.ForeignKey(owner,on_delete=models.CASCADE,default="-100")#the owner object is linked as a foreign key here
    age=models.IntegerField(default="0")#age of the pet
    breed=models.CharField(max_length=30,default="none")#this is used to store the breed of the pet
    pet_type=models.CharField(max_length=5,choices=(('dog','dog'),('cat','cat'),('bird','bird')),default="none")#this is used for pet type the choices option of the charfield is used to provide a dropdown in the django model forms
    sex=models.CharField(max_length=1,default='M')#this is used to store sex of the pet

    