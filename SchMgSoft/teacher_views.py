from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Teacher, Teacher_Notification

# Create your views here.


@login_required(login_url='/')
def HOME(request):
    return render(request, 'teacher/home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    teacher = Teacher.objects.filter(admin=request.user.id)

    for i in teacher:
        teacher_id = i.id
        notifications = Teacher_Notification.objects.filter(teacher_id=teacher_id)

        context = {
            'notifications': notifications
        }
    return render(request, 'teacher/notifications.html', context)




@login_required(login_url='/')
def VIEW_NOTIFICATION(request, id):
    notification = Teacher_Notification.objects.get(id=id)
    teacher = Teacher.objects.filter(admin=request.user.id)

    for i in teacher:
        teacher_id = i.id
        notifications = Teacher_Notification.objects.filter(teacher_id=teacher_id)

    notification.status = 1
    notification.save()

    context = {
        'notification': notification,
        'notifications': notifications
    }

    return render(request, 'teacher/notifications.html', context)