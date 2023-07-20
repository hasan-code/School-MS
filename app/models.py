from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class CustomUser(AbstractUser):
    USER = (
        (1, 'ADMIN'),
        (2, 'TEACHER'),
        (3, 'STUDENT')
    )

    user_type = models.CharField(choices=USER, max_length=20, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)



class Class(models.Model):
    class_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.class_name



class Session(models.Model):
    start_session = models.CharField(max_length=100)
    end_session = models.CharField(max_length=100)

    def __str__(self):
        return self.start_session + " to " + self.end_session
    


class Subject(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    subject_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.class_id.class_name + '-' + self.subject_name
    


# STUDENT MODEL
class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=20)
    dob = models.DateField()
    mobile_no = models.PositiveIntegerField()
    alt_mobile_no = models.PositiveIntegerField()
    aadhaar_no = models.PositiveBigIntegerField()
    vill_town = models.CharField(max_length=200)
    post_office = models.CharField(max_length=200)
    police_station = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    gaon_panchayat = models.CharField(max_length=200)
    educational_block = models.CharField(max_length=200)
    cluster = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pin = models.PositiveIntegerField()
    registration_no = models.CharField(max_length=100)
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    bank_name = models.CharField(max_length=350)
    account_no = models.PositiveIntegerField()
    branch_name = models.CharField(max_length=350)
    ifsc = models.CharField(max_length=100)
    student_photo = models.ImageField(upload_to='media/profile_pic')
    dob_certificate = models.FileField(upload_to='media/students/certificates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    


# TEACHER MODEL
class Teacher(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    qualification = models.TextField()
    sex = models.CharField(max_length=20)
    dob = models.DateField()
    mobile_no = models.PositiveIntegerField()
    pan_no = models.CharField(max_length=10)
    aadhaar_no = models.PositiveBigIntegerField()
    vill_town = models.CharField(max_length=200)
    post_office = models.CharField(max_length=200)
    police_station = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pin = models.PositiveIntegerField()
    bank_name = models.CharField(max_length=350)
    account_no = models.PositiveIntegerField()
    branch_name = models.CharField(max_length=350)
    ifsc = models.CharField(max_length=100)
    teacher_photo = models.ImageField(upload_to='media/profile_pic')
    cv_resume = models.FileField(upload_to='media/teachers/certificates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    

# TEACHER + SUBJECT + CLASS + SESSION - ALLOTMENT MODEL
class Teacher_Allotment(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.teacher_id.admin.first_name + '-' + self.subject_id.subject_name + "," + self.class_id.class_name




# NOTIFICATIONS SEND TO TEACHERS BY ADMIN
class Teacher_Notification(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.TimeField(auto_now_add=True)
    

    def __str__(self):
        return self.teacher_id.admin.first_name + " " + self.teacher_id.admin.last_name
    

# NOTIFICATIONS SEND TO STUDENTS BY ADMIN
class Student_Notification(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.TimeField(auto_now_add=True)
    

    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name
    



# LEAVE APPLY - TEACHER
class Teacher_Leave_Apply(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    leave_date = models.DateField()
    subject = models.CharField(max_length=1000)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher_id.admin.first_name + " " + self.teacher_id.admin.last_name
    


# LEAVE APPLY - STUDENT
class Student_Leave_Apply(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    leave_date = models.DateField()
    subject = models.CharField(max_length=1000)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name
    


# STUDENT'S ATTENDANCE
class Student_Attendance(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_id.subject_name
    

class Student_Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Student_Attendance, on_delete=models.CASCADE)
    attendance_status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name
    

# TEACHER'S ATTENDANCE
class Teacher_Attendance(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    attendance_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Attendance - {self.teacher_id.admin.first_name} {self.teacher_id.admin.last_name}"


# STUDY MATERIALS
class Study_Material(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to='media/study_materials')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.class_id.class_name + "-" + self.subject_id.subject_name + ": Study Materials"
    


# SALARY
class Salary(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    salary_type = models.CharField(max_length=10)
    basic = models.IntegerField()
    hra = models.IntegerField()
    lta = models.IntegerField()
    other_allowance = models.IntegerField()
    bonus = models.IntegerField()
    pf = models.IntegerField()
    gratuity = models.IntegerField()
    other = models.IntegerField()

    def __str__(self):
        return f"Salary - {self.teacher_id.admin.first_name} {self.teacher_id.admin.last_name}"
