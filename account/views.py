from django.shortcuts import render
from .forms import RegistarionForm
# Create your views here.

def home(request):
    return render(request,'authentication/home.html')


def register_view(request):

    form = RegistarionForm()
    context = {
        'form':form
    }

    return render(request,'authentication/register.html',context)