from django.shortcuts import render, redirect
from authentication.models import User_Details
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# sa = signin as, ra = register as.
# views for signin page:
def signin(request):
    if 'user_id' in request.session:
        return redirect('student-home')
    else:
        if request.method == "POST":
            sa = request.POST.get('class')
            mail = request.POST.get('email')
            passwd = request.POST.get('password')
            try:
                user = User_Details.objects.get(email = mail)
                # user = authenticate(request, email = mail, password = pd)
                # print(user)
                if check_password(passwd, user.password):
                    print("password matched")
                    request.session['user_id'] = user.id
                    # login(request, user)
                    if sa == 'Student':
                        return redirect('student-home')
                    if sa == 'Tutor':
                        return redirect('teacher-profile', user.first_name)
                else:
                    return HttpResponse("Invalid password.")
            except Exception as e:
                print(e)
                return HttpResponse("UserEmail does not exist. Please register.")
    return render(request, 'signin.html')

# views for signup page:
def registration(request):
    if 'user_id' in request.session:
        return redirect('student-home')
    else:
        if request.method=="POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            ra = request.POST.get("class")

            hashed_password = make_password(password)
            if ra=="student":
                print("registration as", ra)
                user = User_Details.objects.filter(email = email)
                if user:
                    return HttpResponse('You already have an account!')
                else:
                    instance = User_Details(first_name=first_name, last_name=last_name, email=email, password=hashed_password, is_student=True, type="S")
                    instance.save()
                    
                    current_user = User_Details.objects.get(email=email)
                    user_group = Group.objects.get(name='Student')
                    current_user.groups.add(user_group)
                return redirect('signin')
            if ra=="tutor":
                print("registration as", ra)
                user = User_Details.objects.filter(email = email)
                if user:
                    return HttpResponse('You already have an account!')
                else:
                    instance = User_Details(first_name=first_name, last_name=last_name, email=email, password=hashed_password, is_teacher=True, type="T")
                    instance.save()
                    current_user = User_Details.objects.get(email = email)
                    user_group = Group.objects.get(name='Teacher')
                    current_user.groups.add(user_group)
                return redirect('signin')
                
    return render(request, "registration.html")

