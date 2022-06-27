from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
def logdisp(request):
    return render(request, 'logdisp.html')

def registerdisp(request):
    return render(request, 'reg.html')

def logindisp(request):
    return render(request, 'logindisp.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'This user already exists')
                return redirect(registerdisp)
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'This email is already used')
                return redirect(registerdisp)
            else:
                users = User.objects.create_user(username = username, first_name = firstname, 
                last_name = lastname, password = password1, email = email)
                users.save()
                print('user created')
                messages.info(request, 'User created')
                return redirect(logindisp)
        else:
            messages.info(request, "Passwords don't match")
            return redirect(registerdisp)
    else:
        return render (request, 'reg.html')

# User is the default table created by django while migrating the database.
# Here we use that table to as a database for saving register credentials.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login (request, user)
            return redirect('tra')
            # return render(request, 'index1.html')
        else:
            messages.info(request, "This username or password is incoorect")
            return redirect(logindisp)

    else:
        return render(logindisp)


def logout(request):
    auth.logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect('logdisp')
    #logdisp is the name of 1st path in urls.py
    # redirect(logindisp) is same