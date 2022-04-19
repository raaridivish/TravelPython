from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pswrd = request.POST['pswrd']
        user = auth.authenticate(username=uname, password=pswrd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Login')
            return redirect('login')
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email_id = request.POST['email_id']
        pswrd = request.POST['pswrd']
        cnf_pswrd = request.POST['cnf_pswrd']
        if pswrd == cnf_pswrd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username taken")
                return redirect('registration')

            elif User.objects.filter(email=email_id).exists():
                messages.info(request, "Email id taken")
                return redirect('registration')

            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email_id,
                                                password=pswrd)
                user.save()
                print("User Created")
                return redirect('login')
        else:
            messages.info(request, "passwords not matching")
            return redirect('registration')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')