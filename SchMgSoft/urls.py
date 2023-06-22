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

    # Admin's Page Links
    path('home', admin_views.HOME, name='admin_home'),
    # STUDENT'S LINKS
    path('students', admin_views.STUDENTS, name='students'),
    path('students/edit/<str:id>', admin_views.EDIT_STUDENT, name='edit_student'),
    path('students/update', admin_views.UPDATE_STUDENT, name='update_student'),
    path('students/detete/<str:admin>', admin_views.DELETE_STUDENT, name='delete_student'),
    # TEACHER'S LINKS
    path('teachers', admin_views.TEACHERS, name='teachers'),
    path('teachers/edit/<str:id>', admin_views.EDIT_TEACHER, name='edit_teacher'),
    path('teachers/update', admin_views.UPDATE_TEACHER, name='update_teacher'),
    path('teachers/detete/<str:admin>', admin_views.DELETE_TEACHER, name='delete_teacher'),
    # STAFF MANAGEMENT LINKS
    path('notify_teachers/', admin_views.NOTIFY_TEACHERS, name="notify_teachers"),
    path('notify_teachers/<str:id>', admin_views.SEND_NOTIFICATIONS_TEACHERS, name="send_notifications_teachers"),
    path('notify_students/', admin_views.NOTIFY_STUDENTS, name="notify_students"),
    path('notify_students/<str:id>', admin_views.SEND_NOTIFICATIONS_STUDENTS, name="send_notifications_students"),
    
    path('teacher_leave', admin_views.TEACHER_LEAVE, name="teacher_leave"),
    path('teacher_leave/view/<str:id>', admin_views.VIEW_TEACHER_LEAVE_APPLICATION, name="view_teacher_leave_application"),
    path('teacher_leave/view/approve/<str:id>', admin_views.TEACHER_LEAVE_APPLICATION_APPROVE, name="teacher_leave_application_approve"),
    path('teacher_leave/view/disapprove/<str:id>', admin_views.TEACHER_LEAVE_APPLICATION_DISAPPROVE, name="teacher_leave_application_disapprove"),

    path('student_leave', admin_views.STUDENT_LEAVE, name="student_leave"),
    path('student_leave/view/<str:id>', admin_views.VIEW_STUDENT_LEAVE_APPLICATION, name="view_student_leave_application"),
    path('student_leave/view/approve/<str:id>', admin_views.STUDENT_LEAVE_APPLICATION_APPROVE, name="student_leave_application_approve"),
    path('student_leave/view/disapprove/<str:id>', admin_views.STUDENT_LEAVE_APPLICATION_DISAPPROVE, name="student_leave_application_disapprove"),


    # Teacher's Page Links
    path('home', teacher_views.HOME, name='teacher_home'),
    path('teacher/notifications', teacher_views.TEACHER_NOTIFICATIONS, name='teacher_notifications'),
    path('teacher/notifications/view/<str:id>', teacher_views.TEACHER_VIEW_NOTIFICATION, name='teacher_view_notification'),
    path('teacher/leave_application', teacher_views.TEACHER_LEAVE_APPLICATION, name='teacher_leave_application'),
    path('teacher/leave_apply', teacher_views.TEACHER_LEAVE_APPLY, name='teacher_leave_apply'),
    path('teacher/attendance', teacher_views.ATTENDANCE, name='attendance'),



    # Student's Page Links
    path('home', student_views.HOME, name='student_home'),
    path('student/notifications', student_views.STUDENT_NOTIFICATIONS, name='student_notifications'),
    path('student/notifications/view/<str:id>', student_views.STUDENT_VIEW_NOTIFICATION, name='student_view_notification'),
    path('student/leave_application', student_views.STUDENT_LEAVE_APPLICATION, name='student_leave_application'),
    path('student/leave_apply', student_views.STUDENT_LEAVE_APPLY, name='student_leave_apply'),

    # Admin's - MANAGEMENT
    # CLASS
    path('management/class/add', admin_views.ADD_CLASS, name='add_class'),
    path('management/class/edit/<str:id>', admin_views.EDIT_CLASS, name='edit_class'),
    path('management/class/update', admin_views.UPDATE_CLASS, name='update_class'),
    path('management/class/delete/<str:id>', admin_views.DELETE_CLASS, name='delete_class'),
    # SESSION
    path('management/session/add', admin_views.ADD_SESSION, name='add_session'),
    path('management/session/edit/<str:id>', admin_views.EDIT_SESSION, name='edit_session'),
    path('management/session/update', admin_views.UPDATE_SESSION, name='update_session'),
    path('management/session/delete/<str:id>', admin_views.DELETE_SESSION, name='delete_session'),
    # SUBJECT
    path('management/subject/add', admin_views.ADD_SUBJECT, name='add_subject'),
    path('management/subject/edit/<str:id>', admin_views.EDIT_SUBJECT, name='edit_subject'),
    path('management/subject/update', admin_views.UPDATE_SUBJECT, name='update_subject'),
    path('management/subject/delete/<str:id>', admin_views.DELETE_SUBJECT, name='delete_subject'),
    # TEACHER ALLOTMENT
    path('management/teacher_allotment', admin_views.TEACHER_ALLOTMENT, name='teacher_allotment'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
