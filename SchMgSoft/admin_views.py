from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Class, Session, CustomUser, Student

# Create your views here.


@login_required(login_url='/')
def home(request):
    return render(request, 'admin/home.html')



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




def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()

    messages.success(request, student.first_name + " " + student.last_name + " has been successfully deleted!")
    return redirect('students')



# Admin's - MANAGEMENT
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