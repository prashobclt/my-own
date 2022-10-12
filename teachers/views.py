from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home page')


def loginfun(request):
    return render(request,'login.html')


def signupFun(request):
    return render(request,'signup.html')


