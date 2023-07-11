from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser, UserModel)
admin.site.register(Class)
admin.site.register(Session)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Teacher_Allotment)
admin.site.register(Teacher_Notification)
admin.site.register(Student_Notification)
admin.site.register(Teacher_Leave_Apply)
admin.site.register(Student_Leave_Apply)
admin.site.register(Student_Attendance)
admin.site.register(Student_Attendance_Report)
admin.site.register(Study_Material)
admin.site.register(Salary)