from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    emp_email = models.CharField(max_length=50)
    phone =  models.IntegerField()
    mobile =  models.IntegerField()
    empid = models.AutoField(primary_key=True)
    address =  models.CharField(max_length=100)
    designation =  models.CharField(max_length=100)

    def __str__(self):
        return self.designation

class Client (models.Model):
    client_name = models.CharField(max_length=30)
    client_name = models.CharField(max_length=30)
    client_name = models.CharField(max_length=30)
    client_email = models.CharField(max_length=50)
    client_phone = models.IntegerField()
    client_mobile = models.IntegerField()
    client_account = models.CharField(max_length=50)
    client_project = models.CharField(max_length=50)
    client_address = models.CharField(max_length=100)

class Deptmaster(Employee):
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    logo = models.ImageField()

class Emp_rate(Deptmaster):
    emp_score = models.IntegerField()

class Dept_rate(Deptmaster):
    dept_score = models.IntegerField()

class Client_rate(Deptmaster):
    client_score = models.IntegerField()