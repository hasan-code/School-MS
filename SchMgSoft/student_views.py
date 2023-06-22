from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Student, Student_Notification, Student_Leave_Apply

# Create your views here.

@login_required(login_url='/')
def HOME(request):
    return render(request, 'student/home.html')




@login_required(login_url='/')
def STUDENT_NOTIFICATIONS(request):
    student = Student.objects.filter(admin=request.user.id)

    for i in student:
        student_id = i.id
        notifications = Student_Notification.objects.filter(student_id=student_id)

        context = {
            'notifications': notifications
        }
    return render(request, 'student/notifications.html', context)




@login_required(login_url='/')
def STUDENT_VIEW_NOTIFICATION(request, id):
    notification = Student_Notification.objects.get(id=id)
    student = Student.objects.filter(admin=request.user.id)

    for i in student:
        student_id = i.id
        notifications = Student_Notification.objects.filter(student_id=student_id)

    notification.status = 1
    notification.save()

    context = {
        'notification': notification,
        'notifications': notifications
    }

    return render(request, 'student/notifications.html', context)



@login_required(login_url='/')
def STUDENT_LEAVE_APPLICATION(request):
    leave_applications = Student_Leave_Apply.objects.all()

    context = {
        'leave_applications': leave_applications
    }
    return render(request, 'student/leave_application.html', context)



@login_required(login_url='/')
def STUDENT_LEAVE_APPLY(request):
    if request.method == "POST":
        leave_date = request.POST.get("leave_date")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        student_id = Student.objects.get(admin=request.user.id)

        leave_application = Student_Leave_Apply (
            student_id = student_id,
            leave_date = leave_date,
            subject = subject,
            message = message
        )
        leave_application.save()
        messages.success(request, "Your leave application has been submitted successfully!")
        return redirect('student_leave_application')
        
    return render(request, 'student/leave_apply.html')