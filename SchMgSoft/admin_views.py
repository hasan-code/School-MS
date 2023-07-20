from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from app.models import Class, Session, Subject, CustomUser, Student, Teacher, Teacher_Notification, Student_Notification, Teacher_Leave_Apply, Student_Leave_Apply, Teacher_Allotment, Student_Attendance, Student_Attendance_Report, Salary, Teacher_Attendance

# Create your views here.


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    teacher_count = Teacher.objects.all().count()

    context = {
        'student_count': student_count,
        'teacher_count': teacher_count
    }

    return render(request, 'admin/home.html', context)


# STUDENT'S MANAGEMENT
@login_required(login_url='/')
def STUDENTS(request):
    classes = Class.objects.all()
    sessions = Session.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        father_name = request.POST.get("fathername")
        mother_name = request.POST.get("mothername")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        sex = request.POST.get("sex")
        dob = request.POST.get("dob")
        mobile_number = request.POST.get("mobilenumber")
        alt_mobile_number = request.POST.get("altmobilenumber")
        aadhaar = request.POST.get("aadhaar")
        vill_town = request.POST.get("villtown")
        post_office = request.POST.get("postoffice")
        police_station = request.POST.get("policestation")
        district = request.POST.get("district")
        gaon_panchayat = request.POST.get("gaonpanchayat")
        educational_block = request.POST.get("educationalblock")
        cluster = request.POST.get("cluster")
        state = request.POST.get("state")
        country = request.POST.get("country")
        pin = request.POST.get("pin")
        reg_number = request.POST.get("regnumber")
        class_id = request.POST.get("classadmitted")
        session_id = request.POST.get("session")
        bank_name = request.POST.get("bankname")
        account_number = request.POST.get("accountnumber")
        branch_name = request.POST.get("branchname")
        ifsc = request.POST.get("ifsc")
        student_photo = request.FILES.get("photo")
        dob_certificate = request.FILES.get("certificate")

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Student with this email already registered!")
            return redirect('students')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "This username is already taken!")
            return redirect('students')
        
        else:
            user = CustomUser (
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                profile_pic = student_photo,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            class_admitted = Class.objects.get(id=class_id)
            session = Session.objects.get(id=session_id)

            student = Student (
                admin = user,
                father_name = father_name,
                mother_name = mother_name,
                sex = sex,
                dob = dob,
                mobile_no = mobile_number,
                alt_mobile_no = alt_mobile_number,
                aadhaar_no = aadhaar,
                vill_town = vill_town,
                post_office = post_office,
                police_station = police_station,
                district = district,
                gaon_panchayat = gaon_panchayat,
                educational_block = educational_block,
                cluster = cluster,
                state = state,
                country = country,
                pin = pin,
                registration_no = reg_number,
                class_id = class_admitted,
                session_id = session,
                bank_name = bank_name,
                account_no = account_number,
                branch_name = branch_name,
                ifsc = ifsc,
                dob_certificate = dob_certificate
            )
            student.save()
            messages.success(request, user.first_name + " " + user.last_name + " has been successfully registered!")
            return redirect('students')


    students = Student.objects.all()
    student_count = Student.objects.count()
       
    context = {
        'classes': classes,
        'sessions': sessions,
        'students': students,
        'student_count': student_count
    }
    return render(request, 'admin/students.html', context)



@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    classes = Class.objects.all()
    sessions = Session.objects.all()
    student = Student.objects.filter(id=id)

    context = {
        'classes': classes,
        'sessions': sessions,
        'student': student
    }
    return render(request, 'admin/edit_student.html', context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == 'POST':
        student_id = request.POST.get("student_id")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        father_name = request.POST.get("fathername")
        mother_name = request.POST.get("mothername")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        sex = request.POST.get("sex")
        dob = request.POST.get("dob")
        mobile_number = request.POST.get("mobilenumber")
        alt_mobile_number = request.POST.get("altmobilenumber")
        aadhaar = request.POST.get("aadhaar")
        vill_town = request.POST.get("villtown")
        post_office = request.POST.get("postoffice")
        police_station = request.POST.get("policestation")
        district = request.POST.get("district")
        gaon_panchayat = request.POST.get("gaonpanchayat")
        educational_block = request.POST.get("educationalblock")
        cluster = request.POST.get("cluster")
        state = request.POST.get("state")
        country = request.POST.get("country")
        pin = request.POST.get("pin")
        reg_number = request.POST.get("regnumber")
        class_admitted_id = request.POST.get("classadmitted")
        session_id = request.POST.get("session")
        bank_name = request.POST.get("bankname")
        account_number = request.POST.get("accountnumber")
        branch_name = request.POST.get("branchname")
        ifsc = request.POST.get("ifsc")
        student_photo = request.FILES.get("photo")
        dob_certificate = request.FILES.get("certificate")

        user = CustomUser.objects.get(id=student_id)
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if student_photo != None and student_photo != "":
            user.profile_pic = student_photo

        user.save()


        student = Student.objects.get(admin=student_id)
        student.father_name = father_name
        student.mother_name = mother_name
        student.sex = sex
        student.dob = dob
        student.mobile_no = mobile_number
        student.alt_mobile_no = alt_mobile_number
        student.aadhaar_no = aadhaar
        student.vill_town = vill_town
        student.post_office = post_office
        student.police_station = police_station
        student.district = district
        student.gaon_panchayat = gaon_panchayat
        student.educational_block = educational_block
        student.cluster = cluster
        student.state = state
        student.country = country
        student.pin = pin
        student.registration_no = reg_number

        class_id = Class.objects.get(id=class_admitted_id)
        student.class_id = class_id

        session = Session.objects.get(id=session_id)
        student.session_id = session

        student.bank_name = bank_name
        student.account_no = account_number
        student.branch_name = branch_name
        student.ifsc = ifsc

        if dob_certificate != None and dob_certificate != "":
            student.dob_certificate = dob_certificate

        student.save()
        messages.success(request, user.first_name + " " + user.last_name + "'s data have been updated successfully!")
        return redirect('students')
    
    return render(request, 'admin/edit_student.html')




@login_required(login_url='/')
def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()

    messages.success(request, student.first_name + " " + student.last_name + " has been successfully deleted!")
    return redirect('students')



# TECAHER'S MANAGEMENT
@login_required(login_url='/')
def TEACHERS(request):
    if request.method == 'POST':
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        qualification = request.POST.get("qualification")
        sex = request.POST.get("sex")
        dob = request.POST.get("dob")
        mobile_number = request.POST.get("mobilenumber")
        pan = request.POST.get("pan")
        aadhaar = request.POST.get("aadhaar")
        vill_town = request.POST.get("villtown")
        post_office = request.POST.get("postoffice")
        police_station = request.POST.get("policestation")
        district = request.POST.get("district")
        state = request.POST.get("state")
        country = request.POST.get("country")
        pin = request.POST.get("pin")
        bank_name = request.POST.get("bankname")
        account_number = request.POST.get("accountnumber")
        branch_name = request.POST.get("branchname")
        ifsc = request.POST.get("ifsc")
        photo = request.FILES.get("photo")
        certificate = request.FILES.get("certificate")

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Teacher with this email already appointed!")
            return redirect('teachers')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "This username is already taken!")
            return redirect('teachers')
        
        else:
            user = CustomUser (
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                profile_pic = photo,
                user_type = 2
            )
            user.set_password(password)
            user.save()

            teacher = Teacher (
                admin = user,
                qualification = qualification,
                sex = sex,
                dob = dob,
                mobile_no = mobile_number,
                pan_no = pan,
                aadhaar_no = aadhaar,
                vill_town = vill_town,
                post_office = post_office,
                police_station = police_station,
                district = district,
                state = state,
                country = country,
                pin = pin,
                bank_name = bank_name,
                account_no = account_number,
                branch_name = branch_name,
                ifsc = ifsc,
                cv_resume = certificate
            )
            teacher.save()
            messages.success(request, user.first_name + " " + user.last_name + " has been successfully appointed!")
            return redirect('teachers')


    teachers = Teacher.objects.all()
    teacher_count = Teacher.objects.count()
       
    context = {
        'teachers': teachers,
        'teacher_count': teacher_count
    }
    return render(request, 'admin/teachers.html', context)



@login_required(login_url='/')
def EDIT_TEACHER(request, id):
    teacher = Teacher.objects.filter(id=id)

    context = {
        'teacher': teacher
    }
    return render(request, 'admin/edit_teacher.html', context)



@login_required(login_url='/')
def UPDATE_TEACHER(request):
    if request.method == 'POST':
        teacher_id = request.POST.get("teacher_id")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        qualification = request.POST.get("qualification")
        sex = request.POST.get("sex")
        dob = request.POST.get("dob")
        mobile_number = request.POST.get("mobilenumber")
        pan = request.POST.get("pan")
        aadhaar = request.POST.get("aadhaar")
        vill_town = request.POST.get("villtown")
        post_office = request.POST.get("postoffice")
        police_station = request.POST.get("policestation")
        district = request.POST.get("district")
        state = request.POST.get("state")
        country = request.POST.get("country")
        pin = request.POST.get("pin")
        bank_name = request.POST.get("bankname")
        account_number = request.POST.get("accountnumber")
        branch_name = request.POST.get("branchname")
        ifsc = request.POST.get("ifsc")
        photo = request.FILES.get("photo")
        certificate = request.FILES.get("certificate")

        user = CustomUser.objects.get(id=teacher_id)
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if photo != None and photo != "":
            user.profile_pic = photo

        user.save()


        teacher = Teacher.objects.get(admin=teacher_id)
        teacher.qualification = qualification
        teacher.sex = sex
        teacher.dob = dob
        teacher.mobile_no = mobile_number
        teacher.pan_no = pan
        teacher.aadhaar_no = aadhaar
        teacher.vill_town = vill_town
        teacher.post_office = post_office
        teacher.police_station = police_station
        teacher.district = district
        teacher.state = state
        teacher.country = country
        teacher.pin = pin
        teacher.bank_name = bank_name
        teacher.account_no = account_number
        teacher.branch_name = branch_name
        teacher.ifsc = ifsc

        if certificate != None and certificate != "":
            teacher.cv_resume = certificate

        teacher.save()
        messages.success(request, user.first_name + " " + user.last_name + "'s data have been updated successfully!")
        return redirect('teachers')
    
    return render(request, 'admin/edit_teacher.html')


@login_required(login_url='/')
def DELETE_TEACHER(request, admin):
    teacher = CustomUser.objects.get(id=admin)
    teacher.delete()

    messages.success(request, teacher.first_name + " " + teacher.last_name + " has been successfully deleted!")
    return redirect('teachers')



# ATTENDANCES
@login_required(login_url='/')
def ATTENDANCES(request):
    return render(request, 'admin/attendances.html')



@login_required(login_url='/')
def TAKE_TEACHER_ATTENDANCE(request):
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        date = request.POST.get("date")
        selected_date = datetime.strptime(date, "%Y-%m-%d")
        year = selected_date.year
        month = selected_date.month
        day = selected_date.day
        teacher_ids = request.POST.getlist("teacher_id[]")
        attendance_type_list = []

        for i, teacher_id in enumerate(teacher_ids):
            teacher = Teacher.objects.get(id=teacher_id)
            attendance_status = request.POST.get(f"attendance{i+1}")
            attendance_type_list.append(attendance_status)

            teacher_attendance = Teacher_Attendance (
                teacher_id=teacher,
                day=day,
                month=month,
                year=year,
                attendance_type=attendance_status
            )
            teacher_attendance.save()

        messages.success(request, "Attendances saved successfully!")
        return redirect('attendances')

    context = {
        'teachers': teachers
    }
    return render(request, 'admin/teacher_attendance.html', context)




@login_required(login_url='/')
def VIEW_STUDENT_ATTENDANCE(request):
    classes = Class.objects.all()
    sessions = Session.objects.all()
    subjects = Subject.objects.all()

    action = request.GET.get('action')

    get_class = None
    get_session = None
    get_subject = None
    attendance_reports = None

    if action is not None:
        if request.method == 'POST':
            class_id = request.POST.get("class")
            subject_id = request.POST.get("subject")
            session_id = request.POST.get("session")

            get_class = Class.objects.get(id=class_id)
            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session.objects.get(id=session_id)

            attendance = Student_Attendance.objects.filter(class_id=get_class, subject_id=get_subject, session_id=get_session)

            students = Student.objects.filter(class_id=get_class, session_id=get_session)
            attendance_reports = []
            for student in students:
                total_days = attendance.filter(student_attendance_report__student_id=student.id).count()
                present_days = attendance.filter(student_attendance_report__student_id=student.id, student_attendance_report__attendance_status=1).count()
                absent_days = attendance.filter(student_attendance_report__student_id=student.id, student_attendance_report__attendance_status=0).count()
                percentage = (present_days / total_days) * 100 if total_days != 0 else 0
                
                attendance_reports.append({
                    'student': student,
                    'total_days': total_days,
                    'present_days': present_days,
                    'absent_days': absent_days,
                    'percentage': percentage
                })

    context = {
        'classes': classes,
        'sessions': sessions,
        'subjects': subjects,
        'action': action,
        'attendance_reports': attendance_reports
    }

    return render(request, 'admin/student_attendance.html', context)




# ALLOT CLASS, SUBJECT, SESSION TO TEACHERS
@login_required(login_url='/')
def TEACHER_ALLOTMENT(request):
    if request.method == "POST":
        teacher_id = request.POST.get("teacher")
        class_id = request.POST.get("class")
        subject_id = request.POST.get("subject")
        session_id = request.POST.get("session")

        teacher_selected = Teacher.objects.get(id=teacher_id)
        class_selected = Class.objects.get(id=class_id)
        subject_selected = Subject.objects.get(id=subject_id)
        session_selected = Session.objects.get(id=session_id)

        teacher_allotment = Teacher_Allotment (
            teacher_id = teacher_selected,
            class_id = class_selected,
            subject_id = subject_selected,
            session_id = session_selected
        )
        teacher_allotment.save()
        messages.success(request, subject_selected.subject_name + " has been alloted to " + teacher_selected.admin.first_name + " " + teacher_selected.admin.last_name + " successfully!")
        return redirect('teacher_allotment')
    
    teachers = Teacher.objects.all()
    classes = Class.objects.all()
    subjects = Subject.objects.all()
    sessions = Session.objects.all()
    allotted_teachers = Teacher_Allotment.objects.all()

    context = {
        'teachers': teachers,
        'classes': classes,
        'subjects': subjects,
        'sessions': sessions,
        'allotted_teachers': allotted_teachers
    }

    return render(request, 'admin/teacher_allotment.html', context)




# STAFF MANAGEMENT - ADMIN : SEND NOTIFICATIONS to TEACHERS & STUDENTS
@login_required(login_url='/')
def NOTIFY_TEACHERS(request):
    teachers = Teacher.objects.all()
    teachers_notifications = Teacher_Notification.objects.all()

    context = {
        'teachers': teachers,
        'teachers_notifications': teachers_notifications
    }
    return render(request, 'admin/notify_teachers.html', context)


@login_required(login_url='/')
def SEND_NOTIFICATIONS_TEACHERS(request, id):
    recepient_id = Teacher.objects.get(id=id)

    if request.method == "POST":
        receiver = request.POST.get("receiver")
        message = request.POST.get("message")

        notification = Teacher_Notification (
            teacher_id = recepient_id,
            message = message
        )
        notification.save()
        messages.success(request, "Notification sent to " + receiver + " successfully!")
        return redirect('notify_teachers')

    context = {
        'recepient_id': recepient_id
    }

    return render(request, 'admin/notifications.html', context)


@login_required(login_url='/')
def NOTIFY_STUDENTS(request):
    students = Student.objects.all()
    students_notifications = Student_Notification.objects.all()

    context = {
        'students': students,
        'students_notifications': students_notifications
    }
    return render(request, 'admin/notify_students.html', context)


@login_required(login_url='/')
def SEND_NOTIFICATIONS_STUDENTS(request, id):
    recepient_id = Student.objects.get(id=id)

    if request.method == "POST":
        receiver = request.POST.get("receiver")
        message = request.POST.get("message")

        notification = Student_Notification (
            student_id = recepient_id,
            message = message
        )
        notification.save()
        messages.success(request, "Notification sent to " + receiver + " successfully!")
        return redirect('notify_students')

    context = {
        'recepient_id': recepient_id
    }

    return render(request, 'admin/notifications.html', context)



@login_required(login_url='/')
def TEACHER_LEAVE(request):
    teacher_leave_applications = Teacher_Leave_Apply.objects.all()

    context = {
        'teacher_leave_applications': teacher_leave_applications
    }
    return render(request, 'admin/teacher_leave.html', context)



@login_required(login_url='/')
def VIEW_TEACHER_LEAVE_APPLICATION(request,id):
    leave_application = Teacher_Leave_Apply.objects.get(id=id)

    context = {
        'leave_application': leave_application
    }
    return render(request, 'admin/view_teacher_leave_application.html', context)



@login_required(login_url='/')
def TEACHER_LEAVE_APPLICATION_APPROVE(request,id):
    leave_application = Teacher_Leave_Apply.objects.get(id=id)
    leave_application.status = 1
    leave_application.save()

    return redirect('teacher_leave')



@login_required(login_url='/')
def TEACHER_LEAVE_APPLICATION_DISAPPROVE(request,id):
    leave_application = Teacher_Leave_Apply.objects.get(id=id)
    leave_application.status = 2
    leave_application.save()

    return redirect('teacher_leave')




@login_required(login_url='/')
def STUDENT_LEAVE(request):
    student_leave_applications = Student_Leave_Apply.objects.all()

    context = {
        'student_leave_applications': student_leave_applications
    }
    return render(request, 'admin/student_leave.html', context)



@login_required(login_url='/')
def VIEW_STUDENT_LEAVE_APPLICATION(request,id):
    leave_application = Student_Leave_Apply.objects.get(id=id)

    context = {
        'leave_application': leave_application
    }
    return render(request, 'admin/view_student_leave_application.html', context)



@login_required(login_url='/')
def STUDENT_LEAVE_APPLICATION_APPROVE(request,id):
    leave_application = Student_Leave_Apply.objects.get(id=id)
    leave_application.status = 1
    leave_application.save()

    return redirect('student_leave')



@login_required(login_url='/')
def STUDENT_LEAVE_APPLICATION_DISAPPROVE(request,id):
    leave_application = Student_Leave_Apply.objects.get(id=id)
    leave_application.status = 2
    leave_application.save()

    return redirect('student_leave')


# FINANCE SECTIONS
@login_required(login_url='/')
def SALARY(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers
    }
    return render(request, 'admin/salary.html', context)



@login_required(login_url='/')
def ADD_SALARY(request):
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        teacher_id = request.POST.get("teacher")
        salary_type = request.POST.get("salary_type")
        basic = request.POST.get("basic")
        hra = request.POST.get("hra")
        lta = request.POST.get("lta")
        other_allowance = request.POST.get("other_allowance")
        bonus = request.POST.get("bonus")
        pf = request.POST.get("pf")
        gratuity = request.POST.get("gratuity")
        other = request.POST.get("other")

        teacher = Teacher.objects.get(id=teacher_id)

        salary = Salary (
            teacher_id=teacher,
            salary_type=salary_type,
            basic=basic,
            hra=hra,
            lta=lta,
            other_allowance=other_allowance,
            bonus=bonus,
            pf=pf,
            gratuity=gratuity,
            other=other
        )
        salary.save()
        messages.success(request, f"{teacher}\'s salary has been successfully saved!")

    context = {
        'teachers': teachers
    }
    return render(request, 'admin/add_salary.html', context)

# Admin's - MANAGEMENT
# CLASS
@login_required(login_url='/')
def ADD_CLASS(request):
    if request.method == 'POST':
        add_class = request.POST.get("add_class")

        class_name = Class (
            class_name = add_class
        )
        
        class_name.save()
        messages.success(request, class_name.class_name + " is added successfully!")
        return redirect('add_class')


    classes = Class.objects.all()
    context = {
        'classes': classes
    }
    return render(request, 'admin/add_class.html', context)


@login_required(login_url='/')
def EDIT_CLASS(request, id):
    classes = Class.objects.get(id=id)

    context = {
        'classes': classes
    }
    return render(request, 'admin/edit_class.html', context)



@login_required(login_url='/')
def UPDATE_CLASS(request):
    if request.method == 'POST':
        class_id = request.POST.get("class_id")
        editted_class_name = request.POST.get("edit_class")


        class_name_to_be_edited = Class.objects.get(id=class_id)
        class_name_to_be_edited.class_name = editted_class_name
        class_name_to_be_edited.save()
        messages.success(request, "Class name has been updated successfully!")
        return redirect('add_class')
    
    return render(request, 'admin/edit_class.html')



@login_required(login_url='/')
def DELETE_CLASS(request, id):
    classes = Class.objects.get(id=id)
    classes.delete()
    messages.success(request, classes.class_name + " has been deleted successfully!")

    return redirect('add_class')


# SESSION
@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == 'POST':
        start_session = request.POST.get("start_session")
        end_session = request.POST.get("end_session")

        session = Session (
            start_session = start_session,
            end_session = end_session
        )
        
        session.save()
        messages.success(request, "Session is created successfully!")
        return redirect('add_session')


    sessions = Session.objects.all()
    context = {
        'sessions': sessions
    }
    return render(request, 'admin/add_session.html', context)



@login_required(login_url='/')
def EDIT_SESSION(request, id):
    session = Session.objects.get(id=id)

    context = {
        'session': session
    }
    return render(request, 'admin/edit_session.html', context)



@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == 'POST':
        session_id = request.POST.get("session_id")
        start_session = request.POST.get("start_session")
        end_session = request.POST.get("end_session")


        session = Session.objects.get(id=session_id)
        session.start_session = start_session
        session.end_session = end_session
        session.save()
        messages.success(request, "Session has been updated successfully!")
        return redirect('add_session')
    
    return render(request, 'admin/edit_session.html')



@login_required(login_url='/')
def DELETE_SESSION(request, id):
    session = Session.objects.get(id=id)
    session.delete()
    messages.success(request, "Session has been deleted successfully!")

    return redirect('add_session')


# SUBJECT
@login_required(login_url='/')
def ADD_SUBJECT(request):
    if request.method == 'POST':
        class_id = request.POST.get("class")
        add_subject = request.POST.get("add_subject")

        class_selected = Class.objects.get(id=class_id)

        subject = Subject (
            class_id = class_selected,
            subject_name = add_subject
        )
        
        subject.save()
        messages.success(request, subject.subject_name + " is added successfully!")
        return redirect('add_subject')


    classes = Class.objects.all()
    subjects = Subject.objects.all()
    context = {
        'classes': classes,
        'subjects': subjects
    }
    return render(request, 'admin/add_subject.html', context)



@login_required(login_url='/')
def EDIT_SUBJECT(request, id):
    subject = Subject.objects.get(id=id)
    classes = Class.objects.all()

    context = {
        'subject': subject,
        'classes': classes
    }
    return render(request, 'admin/edit_subject.html', context)



@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == 'POST':
        subject_id = request.POST.get("subject_id")
        class_id = request.POST.get("class")
        subject_name = request.POST.get("edit_subject")

        class_selected = Class.objects.get(id=class_id)
        subject = Subject.objects.get(id=subject_id)

        subject.class_id = class_selected
        subject.subject_name = subject_name
        subject.save()
        messages.success(request, "Subject has been updated successfully!")
        return redirect('add_subject')
    
    return render(request, 'admin/edit_subject.html')



@login_required(login_url='/')
def DELETE_SUBJECT(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    messages.success(request, "Subject has been deleted successfully!")

    return redirect('add_subject')
