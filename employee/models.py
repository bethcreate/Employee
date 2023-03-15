from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length=200, null=True)
    password= models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)


