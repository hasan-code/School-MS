from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

# Create your views here.


def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))

        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
            elif user_type == '2':
                return redirect('teacher_home')
            elif user_type == '3':
                return HttpResponse("This is Student's panel.")
            else:
                # Error message
                messages.error(request, "The email or password you've entered may be incorrect. Please try again!")
                return redirect('login')
        else:
            # Error message
            messages.error(request, "The email or password you've entered may be incorrect. Please try again!")
            return redirect('login')
        


def doLogout(request):
    logout(request)
    return redirect('login')



# Update Profile Views
@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)



@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profilePic')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        city = request.POST.get('city')
        country = request.POST.get('country')

        # print(profile_pic, first_name, last_name, city, country)
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.city = city
            customuser.country = country

            customuser.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')

        except:
            messages.error(request, "Failed to update your profile!")
    return render(request, 'profile.html')