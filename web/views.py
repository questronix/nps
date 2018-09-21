from django.shortcuts import render


def home(request):
    return render(request, 'web/home.html')

def login(request):
    return render(request, 'web/login.html')

def departmentlist(request):
    return render(request, 'web/department_list.html')

def ratingpage(request):
    return render(request, 'web/rating_page.html')

def clientrequirement(request):
    return render(request, 'web/client_requirement.html')
