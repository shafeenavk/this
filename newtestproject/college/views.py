from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Department,Course
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User(username=username, password=password)
        user.save()

    return render(request, "login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        user=User(username=username,password=password)
        user.save()
        return redirect("/login")
    return render(request,"register.html")


def dropdown(request):
    departmentid=request.GET.get("department",None)
    courseid = request.GET.get("course", None)
    course=None
    if departmentid:
        getdepartment = Department.objects.get(id=departmentid)
        course = Course.objects.filter(department=getdepartment)
    if courseid:
        getcourse=Course.objects.get(id=courseid)
    department=Department.objects.all()
    courses=Course.objects.all()
    return render(request,'dropdown.html',locals())
def submit(request):
    return render(request,'submit.html')