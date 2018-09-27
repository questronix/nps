from django.shortcuts import render, redirect
from .models import Employee
from django.contrib import messages

employ = [
    {
        'empid': '',
        'first_name': '',
        'middle_name': '',
        'last_name': '',
        'emp_email': '',
        'phone': '',
        'mobile': '',
        'address': '',
        'designation': '',
        'department': '',
    }
]


def home(request):
    return render(request, 'web/home.html')


def login(request):
    return render(request, 'web/login.html')


def departmentlist(request):
    context = {
        'employ': Employee.objects.all()
    }
    return render(request, 'web/department_list.html', context)


def ratingpage(request):
    return render(request, 'web/rating_page.html')


def clientrequirement(request):
    return render(request, 'web/client_requirement.html')


def register(request):
    return render(request, 'web/register.html')