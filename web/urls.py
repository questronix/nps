from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
<<<<<<< HEAD
    path('login/', views.login, name='web-login'),
=======
    path('department_list/', views.departmentlist, name='web-dep'),
    path('rating_page/', views.ratingpage, name='web-rp'),
>>>>>>> initial-rating-page-views
]