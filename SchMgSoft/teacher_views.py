from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Teacher, Teacher_Notification, Teacher_Leave_Apply, Student, Class, Session, Subject, Teacher_Allotment, Student_Attendance, Student_Attendance_Report, Study_Material

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
def TEACHER_TAKE_ATTENDANCE(request):
    teacher_id = Teacher.objects.get(admin=request.user.id)
    teacher_allotments = Teacher_Allotment.objects.filter(teacher_id=teacher_id)

    action = request.GET.get('action')
    get_class = None
    get_subject = None
    get_session = None
    
    subjects = []
    classes = []
    sessions = []

    for allotment in teacher_allotments:
        subject = allotment.subject_id
        if subject not in subjects:
            subjects.append(subject)
        
        class_ = allotment.class_id
        if class_ not in classes:
            classes.append(class_)

        session = allotment.session_id
        if session not in sessions:
            sessions.append(session)


        
    if action is not None:
        if request.method == 'POST':
            class_id = request.POST.get("class")
            subject_id = request.POST.get("subject")
            session_id = request.POST.get("session")

            get_class = Class.objects.get(id=class_id)
            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session.objects.get(id=session_id)


    students = Student.objects.filter(class_id=get_class)

    context = {
        'action': action,
        'subjects': subjects,
        'classes': classes,
        'sessions': sessions,
        'get_class': get_class,
        'get_subject': get_subject,
        'get_session': get_session,
        'students': students
    }


    return render(request, 'teacher/take_attendance.html', context)

# @login_required(login_url='/')
# def TAKE_ATTENDANCE(request):
#     teacher_id = Teacher.objects.get(admin=request.user.id)
#     teacher_allotments = Teacher_Allotment.objects.filter(teacher_id=teacher_id)

#     action = request.GET.get('action')
#     get_class = None
#     get_subject = None
#     get_session = None
    
#     subjects = []
#     classes = []
#     sessions = []

#     for allotment in teacher_allotments:
#         subject = allotment.subject_id
#         if subject not in subjects:
#             subjects.append(subject)
        
#         class_ = allotment.class_id
#         if class_ not in classes:
#             classes.append(class_)

#         session = allotment.session_id
#         if session not in sessions:
#             sessions.append(session)


#         if action is not None:
#             if request.method == 'POST':
#                 class_id = request.POST.get("class")
#                 subject_id = request.POST.get("subject")
#                 date = request.POST.get("date")
#                 session_id = request.POST.get("session")

#                 get_class = Class.objects.get(id=class_id)
#                 get_subject = Subject.objects.get(id=subject_id)
#                 get_session = Session.objects.get(id=session_id)

#                 Check if attendance for the selected date, class, subject and session already exists.
#                 attendance_exists = Attendance.objects.filter(
#                     class_id=get_class,
#                     subject_id=get_subject,
#                     attendance_date=date,
#                     session_id=get_session
#                 ).exists()

#                 if attendance_exists:
#                     messages.warning(request, "Attendance for this subject, class and session on this date already exists!")
                    
#                 else:
#                     attendance = Attendance (
#                         class_id = get_class,
#                         subject_id = get_subject,
#                         attendance_date = date,
#                         session_id = get_session
#                     )
#                     attendance.save()
    
#     students = Student.objects.filter(class_id=get_class)

#     context = {
#         'action': action,
#         'subjects': subjects,
#         'classes': classes,
#         'sessions': sessions,
#         'students': students
#     }
    
#     return render(request, 'teacher/take_attendance.html', context)




@login_required(login_url='/')
def TEACHER_SAVE_ATTENDANCE(request):
    if request.method == 'POST':
        class_id = request.POST.get("class")
        subject_id = request.POST.get("subject")
        date = request.POST.get("date")
        session_id = request.POST.get("session")
        student_ids = request.POST.getlist("student_id[]")
        attendance_status_list = []


        get_class = Class.objects.get(id=class_id)
        get_subject = Subject.objects.get(id=subject_id)
        get_session = Session.objects.get(id=session_id)

        attendance = Student_Attendance (
            class_id=get_class,
            subject_id=get_subject,
            attendance_date=date,
            session_id=get_session
        )
        attendance.save()

        for i, student_id in enumerate(student_ids):
            student = Student.objects.get(id=student_id)
            attendance_status = int(request.POST.get(f"attendance{i+1}"))
            attendance_status_list.append(attendance_status)

            attendance_report = Student_Attendance_Report(
                student_id=student,
                attendance_id=attendance,
                attendance_status=attendance_status
            )
            attendance_report.save()
            
    messages.success(request, "Attendances saved successfully!")
    return redirect('teacher_take_attendance')



@login_required(login_url='/')
def TEACHER_VIEW_ATTENDANCE(request):
    teacher_id = Teacher.objects.get(admin=request.user.id)
    teacher_allotments = Teacher_Allotment.objects.filter(teacher_id=teacher_id)

    action = request.GET.get('action')
    get_class = None
    get_subject = None
    get_session = None
    attendance_report = None
    
    subjects = []
    classes = []
    sessions = []

    for allotment in teacher_allotments:
        subject = allotment.subject_id
        if subject not in subjects:
            subjects.append(subject)
        
        class_ = allotment.class_id
        if class_ not in classes:
            classes.append(class_)

        session = allotment.session_id
        if session not in sessions:
            sessions.append(session)


        
    if action is not None:
        if request.method == 'POST':
            class_id = request.POST.get("class")
            subject_id = request.POST.get("subject")
            date = request.POST.get("date")
            session_id = request.POST.get("session")

            get_class = Class.objects.get(id=class_id)
            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session.objects.get(id=session_id)

            attendance = Student_Attendance.objects.filter(
                class_id=get_class,
                subject_id=get_subject,
                attendance_date=date,
                session_id=get_session
                )
            
            for i in attendance:
                attendance_id = i.id
                attendance_report = Student_Attendance_Report.objects.filter(attendance_id=attendance_id)

    students = Student.objects.filter(class_id=get_class)

    context = {
        'action': action,
        'subjects': subjects,
        'classes': classes,
        'sessions': sessions,
        'students': students,
        'attendance_report': attendance_report
    }



    return render(request, 'teacher/view_attendance.html', context)




@login_required(login_url='/')
def TEACHER_STUDY_MATERIALS(request):
    teacher_id = Teacher.objects.get(admin=request.user.id)
    classes = Class.objects.all()
    subjects = Subject.objects.all()
    sessions = Session.objects.all()

    if request.method == "POST":
        class_id = request.POST.get("class")
        subject_id = request.POST.get("subject")
        session_id = request.POST.get("session")
        file = request.FILES.get("file")
        description = request.POST.get("description")


        get_class = Class.objects.get(id=class_id)
        get_subject = Subject.objects.get(id=subject_id)
        get_session = Session.objects.get(id=session_id)

        study_material = Study_Material (
            teacher_id = teacher_id,
            class_id = get_class,
            subject_id = get_subject,
            session_id = get_session,
            file = file,
            description = description
        )
        study_material.save()
        messages.success(request, "Study Material is uploaded successfully!")

    context = {
        'classes': classes,
        'subjects': subjects,
        'sessions': sessions
    }

    return render(request, 'teacher/study_materials.html', context)