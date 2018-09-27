from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    emp_email = models.CharField(max_length=50)
    phone = models.IntegerField()
    mobile = models.IntegerField()
    empid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    logo = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.designation

class Ratings(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    rate = models.IntegerField()
    pass

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    rate = models.IntegerField()
    pass