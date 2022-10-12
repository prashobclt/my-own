from django.shortcuts import render

# Create your views here.
def logofun(request):
    return render(request,'student_template/login.html')