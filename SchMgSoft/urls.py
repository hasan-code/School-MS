"""
URL configuration for SchMgSoft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, admin_views, teacher_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # Login Path
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),

    # Logout Path
    path('doLogout', views.doLogout, name='logout'),

    # Profile Update Path
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # Admin's Page
    path('home', admin_views.home, name='admin_home'),
    path('students', admin_views.STUDENTS, name='students'),
    path('students/edit/<str:id>', admin_views.EDIT_STUDENT, name='edit_student'),
    path('students/update', admin_views.UPDATE_STUDENT, name='update_student'),
    path('students/detete/<str:admin>', admin_views.DELETE_STUDENT, name='delete_student'),

    # Admin's - MANAGEMENT
    path('management/add_class', admin_views.ADD_CLASS, name='add_class'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
