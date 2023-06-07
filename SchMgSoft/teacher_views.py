from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Teacher, Teacher_Notification, Teacher_Leave_Apply

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



@login_required(login_url='/')
def LEAVE_APPLICATION(request):
    leave_applications = Teacher_Leave_Apply.objects.all()

    context = {
        'leave_applications': leave_applications
    }
    return render(request, 'teacher/leave_application.html', context)



@login_required(login_url='/')
def LEAVE_APPLY(request):
    if request.method == "POST":
        leave_date = request.POST.get("leave_date")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        teacher_id = Teacher.objects.get(admin=request.user.id)

        leave_application = Teacher_Leave_Apply (
            teacher_id = teacher_id,
            leave_date = leave_date,
            subject = subject,
            message = message
        )
        leave_application.save()
        messages.success(request, "Your leave application has been submitted successfully!")
        return redirect('leave_application')
        
    return render(request, 'teacher/leave_apply.html')