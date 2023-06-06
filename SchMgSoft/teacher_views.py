from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/')
def HOME(request):
    return render(request, 'teacher/home.html')


@login_required(login_url='/')
def VIEW_NOTIFICATIONS(request):
    return render(request, 'teacher/view_notifications.html')