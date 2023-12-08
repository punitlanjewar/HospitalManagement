from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .models import CustomUser
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        user_name = request.POST['txtUsername']
        user_password = request.POST['txtPassword']
        u1 = authenticate(username=user_name, password=user_password)
        if u1 is not None:
            if u1.is_superuser:
                login(request, u1)
                doctor_details = {
                    'first_name': u1.first_name,
                    'last_name': u1.last_name,
                    'username': u1.username,
                    'email': u1.email,
                    'address': u1.user_address,
                    'lane': u1.user_lane,
                    'city': u1.user_city,
                    'state': u1.user_state,
                    'pincode': u1.user_pincode,
                    'profile_picture': u1.profile_picture,
                }
                # return render(request, 'doctor_home.html', {'DoctorDetails': doctor_details})
                return HttpResponseRedirect('doctor_home', {'DoctorDetails': doctor_details})
            else:
                login(request, u1)
                user_details = {
                    'first_name': u1.first_name,
                    'last_name': u1.last_name,
                    'username': u1.username,
                    'email': u1.email,
                    'address': u1.user_address,
                    'lane': u1.user_lane,
                    'city': u1.user_city,
                    'state': u1.user_state,
                    'pincode': u1.user_pincode,
                    'profile_picture': u1.profile_picture,
                }
                return render(request, 'patient_home.html', {'UserDetails': user_details})
        else:
            return render(request, 'login.html', {'Msg': 'Username and Password Not Matching'}) 
    else:       
        return render(request, 'login.html')
    
def patient_signup_page(request):
    if request.method == 'POST':
        first_name = request.POST['txtFirstName']
        last_name = request.POST['txtLastName']
        profile_picture = request.FILES.get('txtProfilePicture')
        user_name = request.POST['txtUsername']
        email_id = request.POST['txtEmailId']
        password = request.POST['txtPassword']
        confirm_password = request.POST['txtConfirmPassword']
        address = request.POST['txtAddress']
        lane = request.POST['txtLine1']
        city = request.POST['txtCity']
        state = request.POST['txtState']
        pincode = int(request.POST['txtPinCode'])
        if password == confirm_password:
            if CustomUser.objects.filter(username = user_name).exists():
                return render(request, 'patient_signup.html', {'Msg': 'Username already in use please use different'})
            elif CustomUser.objects.filter(email=email_id).exists():
                return render(request, 'patient_signup.html', {'Msg': 'Email already exist use different'})
            else:
                u1 = CustomUser.objects.create_user(
                    first_name = first_name, 
                    last_name = last_name, 
                    username = user_name, 
                    email = email_id, 
                    password = password,
                    user_address = address,
                    user_lane = lane,
                    user_city = city,
                    user_state = state,
                    user_pincode = pincode,
                    profile_picture = profile_picture
                    )
                u1.save()
                return render(request, 'login.html', {'Success1': 'Account Created Successfully'})
        else:
            return render(request, 'patient_signup.html', {'Msg1': 'Password & Confirm Password not matching'})
    else:            
        return render(request, 'patient_signup.html')    

def doctor_signup_page(request):
    if request.method == 'POST':
        first_name = request.POST['txtFirstName1']
        last_name = request.POST['txtLastName1']
        profile_picture = request.FILES.get('txtProfilePicture1')
        user_name = request.POST['txtUsername1']
        email_id = request.POST['txtEmailId1']
        password = request.POST['txtPassword1']
        confirm_password = request.POST['txtConfirmPassword1']
        address = request.POST['txtAddress1']
        lane = request.POST['txtLine1']
        city = request.POST['txtCity1']
        state = request.POST['txtState1']
        pincode = int(request.POST['txtPinCode1'])
        if password == confirm_password:
            if CustomUser.objects.filter(username = user_name).exists():
                return render(request, 'patient_signup.html', {'Msg': 'Username already in use please use different'})
            elif CustomUser.objects.filter(email=email_id).exists():
                return render(request, 'patient_signup.html', {'Msg': 'Email already exist use different'})
            else:
                u1 = CustomUser.objects.create_superuser(
                    first_name=first_name, 
                    last_name=last_name, 
                    username=user_name, 
                    email=email_id, 
                    password=password,
                    user_address = address,
                    user_lane = lane,
                    user_city = city,
                    user_state = state,
                    user_pincode = pincode,
                    profile_picture = profile_picture
                    )
                u1.save()
                return render(request, 'login.html', {'Success1': 'Account Created Successfully'})
        else:
            return render(request, 'doctor_signup.html', {'Msg1': 'Password & Confirm Password not matching'})
    else:            
        return render(request, 'doctor_signup.html')

def doctor_home_page(request):
    return render(request, 'doctor_home.html')

def patient_home_page(request):
    return render(request, 'patient_home.html')

