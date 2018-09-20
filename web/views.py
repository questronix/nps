from django.shortcuts import render

def home(request):
    return render(request, 'web/home.html')

def departmentlist(request):
    return render(request, 'web/department_list.html')

def ratingpage(request):
    return render(request, 'web/rating_page.html')