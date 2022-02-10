from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    despriction = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "department"

class role(models.Model):
    name = models.CharField(max_length=100,null=False)
    despriction = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "role"
    



class Employees(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return self.first_name

class Contact(models.Model):
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(default=0)
    country = models.CharField(max_length=100, null= False)
    subject = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.firstname


