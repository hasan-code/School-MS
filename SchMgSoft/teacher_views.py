from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Teacher, Teacher_Notification, Teacher_Leave_Apply, Student, Class, Session, Subject, Teacher_Allotment, Attendance, Attendance_Save

# Create your views here.


@login_required(login_url='/')
def HOME(request):
    return render(request, 'teacher/home.html')


@login_required(login_url='/')
def TEACHER_NOTIFICATIONS(request):
    teacher = Teacher.objects.filter(admin=request.user.id)

    for i in teacher:
        teacher_id = i.id
        notifications = Teacher_Notification.objects.filter(teacher_id=teacher_id)

        context = {
            'notifications': notifications
        }
    return render(request, 'teacher/notifications.html', context)




@login_required(login_url='/')
def TEACHER_VIEW_NOTIFICATION(request, id):
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
def TEACHER_LEAVE_APPLICATION(request):
    leave_applications = Teacher_Leave_Apply.objects.all()

    context = {
        'leave_applications': leave_applications
    }
    return render(request, 'teacher/leave_application.html', context)



@login_required(login_url='/')
def TEACHER_LEAVE_APPLY(request):
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
        return redirect('teacher_leave_application')
        
    return render(request, 'teacher/leave_apply.html')



@login_required(login_url='/')
def ATTENDANCE(request):
    teacher_id = Teacher.objects.get(admin=request.user.id)
    teacher_allotments = Teacher_Allotment.objects.filter(teacher_id=teacher_id)
    

    action = request.GET.get('action')
    get_class = None
    get_subject = None
    get_session = None
    subjects = []
    classes = []

    for allotment in teacher_allotments:
        subject = allotment.subject_id
        if subject not in subjects:
            subjects.append(subject)
        
        class_ = allotment.class_id
        if class_ not in classes:
            classes.append(class_)

    if action is not None:
        if request.method == 'POST':
            class_id = request.POST.get("class")
            subject_id = request.POST.get("subject")
            date = request.POST.get("date")
            session_id = request.POST.get("session")

            get_class = Class.objects.get(id=class_id)
            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session.objects.get(id=session_id)
            # print(session_id)

            attendance = Attendance (
                class_id = get_class,
                subject_id = get_subject,
                attendance_date = date,
                session_id = get_session
            )

            attendance.save()
            

    
    sessions = Session.objects.all()
    students = Student.objects.filter(class_id=get_class)

    context = {
        'action': action,
        'students': students,
        'subjects': subjects,
        'classes': classes,
        'get_class': get_class,
        'get_subject': get_subject,
        'sessions': sessions,
        'get_session': get_session
    }
    return render(request, 'teacher/attendance.html', context)




@login_required(login_url='/')
def SAVE_ATTENDANCE(request):
    if request.method == 'POST':
        student_ids = request.POST.getlist("student_id[]")
        attendance_status_list = []

        for i, student_id in enumerate(student_ids):
            student = Student.objects.get(id=student_id)
            attendance_status = int(request.POST.get(f"attendance{i+1}"))
            attendance_status_list.append(attendance_status)

            attendance_save = Attendance_Save(
                student_id=student,
                attendance_status=attendance_status
            )
            attendance_save.save()
            
    messages.success(request, "Attendances saved successfully!")
    return redirect('attendance')
