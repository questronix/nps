from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('department_list/', views.departmentlist, name='web-dep'),
    path('rating_page/', views.ratingpage, name='web-rp'),
]