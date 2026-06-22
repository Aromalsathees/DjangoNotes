from django.shortcuts import render, redirect
from .forms import RegistarionForm, LoginForm
from django.contrib.auth import authenticate, login, logout

from .models import Profile
# Create your views here.

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
  

