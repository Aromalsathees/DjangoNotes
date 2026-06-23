from django.shortcuts import render, redirect
from .forms import RegistarionForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required(login_url='login')
def home(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request,'authentication/home.html')


def register_view(request):

    if request.method == 'POST':
        form = RegistarionForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(
                form.cleaned_data["password"]
            )
            user.save()

            # form.save()
            return redirect('home')

    form = RegistarionForm()
    context = {
        'form':form
    }

    return render(request,'authentication/register.html',context)


def Login(request):

    form = LoginForm(request.POST or None)

    if request.method == 'POST':  

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

# checking database 
            user = authenticate(
                request,
                username=email,
                password=password
            )
            if user is not None:
                login(request,user)
                return redirect('home')


    context = {
        'form':form
    }


    return render(request,'authentication/login.html',context)
  


def logout_view(request):
    logout(request)
    return redirect('login')


def profile(request):
    print(request.user)
    print(request.user.is_authenticated)

    if request.method == 'POST':

        profile = Profile.objects.get(user=request.user)

        profile.bio = request.POST.get('bio')
        profile.age = request.POST.get('age')

        profile.save()

        return redirect('home')

    get_user = request.user

    context = {
        'get_user':get_user
    }
    return render(request,'authentication/profile.html',context)