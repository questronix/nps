from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from employee import views as emp_views
from django.contrib.auth import views as auth_viewws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', emp_views.register, name='emp_reg'),
    path('profile/', emp_views.profile, name='profile'),
    path('login/', auth_viewws.LoginView.as_view(template_name='employee/login.html'), name='login'),
    path('logout/', auth_viewws.LogoutView.as_view(template_name='employee/logout.html'), name='logout'),
    path('', include('web.urls', )),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
