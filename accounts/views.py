from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contact.models import Contact

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in now.')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid username and password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):

    if request.method == 'POST':
        #get values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if password match
        if password == password2:
            #check user name
            if User.objects.filter(username=username).exists():
                messages.error(request,'User Already exists.' )
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken.')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,
                    username=username,email=email,password=password)
                    # auth.login(request, user)
                    messages.success(request, 'you are register now and can login.')
                    user.save()
                    return redirect('login')
        else:
            messages.error(request,'Password not match.' )
            return redirect('register')
    else:
        return render(request, 'accounts/registration.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are logged out')
    return redirect('index')

def dashboard(request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts':user_contact
    }
    return render(request, 'accounts/dashboard.html', context)
