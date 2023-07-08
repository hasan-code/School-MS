from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Student, Student_Notification, Student_Leave_Apply, Class, Session, Subject, Attendance, Attendance_Report, Study_Material

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



@login_required(login_url='/')
def ATTENDANCE(request):
    student_id = Student.objects.get(admin=request.user.id)

    action = request.GET.get('action')
    get_class = None
    get_session = None
    attendance_report = None
    subjects = []

    if action is not None:
        if request.method == 'POST':
            class_id = request.POST.get("class")
            session_id = request.POST.get("session")

            get_class = Class.objects.get(id=class_id)
            get_session = Session.objects.get(id=session_id)

            attendance = Attendance.objects.filter(class_id=get_class, session_id=get_session)

            attendance_report = Attendance_Report.objects.filter(student_id=student_id, attendance_id__in=attendance)

    if get_class:
        subjects = Subject.objects.filter(class_id=get_class)

    classes = Class.objects.all()
    sessions = Session.objects.all()
    
    # Calculate attendance statistics for each subject
    subject_statistics = []
    for subject in subjects:
        total_days = Attendance.objects.filter(class_id=get_class, session_id=get_session, subject_id=subject).count()
        present_days = Attendance_Report.objects.filter(student_id=student_id, attendance_id__in=attendance, attendance_status=1, attendance_id__subject_id=subject).count()
        absent_days = Attendance_Report.objects.filter(student_id=student_id, attendance_id__in=attendance, attendance_status=0, attendance_id__subject_id=subject).count()
        if present_days:
            present_percentage = present_days / total_days * 100
        else:
            present_percentage = 0
        subject_statistics.append({
            'subject': subject,
            'total_days': total_days,
            'present_days': present_days,
            'absent_days': absent_days,
            'present_percentage': present_percentage
        })

    context = {
        'action': action,
        'classes': classes,
        'sessions': sessions,
        'subjects': subjects,
        'get_class': get_class,
        'get_session': get_session,
        'attendance_report': attendance_report,
        'subject_statistics': subject_statistics
    }
    return render(request, 'student/attendance.html', context)



@login_required(login_url='/')
def STUDENT_STUDY_MATERIALS(request):
    classes = Class.objects.all()
    sessions = Session.objects.all()

    study_materials = None

    if request.method == 'POST':
        class_id = request.POST.get('class')
        session_id = request.POST.get('session')

        get_class = Class.objects.get(id=class_id)
        get_session = Session.objects.get(id=session_id)

        study_materials = Study_Material.objects.filter(class_id=get_class, session_id=get_session)

    context = {
        'classes': classes,
        'sessions': sessions,
        'study_materials': study_materials
    }
    return render(request, 'student/study_materials.html', context)