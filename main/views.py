from django.shortcuts import render,redirect
from .decorators import check_login,login_required
from django.contrib.auth import logout as auth_logout
from .models import *

@check_login
def login(request):
    return render(request,'login.html')


@login_required
def home(request):
    return render(request,'home.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('main:login')

@login_required
def routinelist(request):
    routins = ClassRoutine.objects.all()
    context = {'routins':routins}
    return render(request,'routinLists.html',context)


@login_required
def createroutine(request):
    classrooms = ClassRoom.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()


    if request.method == 'POST':
        classroom = request.POST['class']
        teacher = request.POST['teacher']
        subject = request.POST['subject']
        start = request.POST['start']
        end = request.POST['end']
        isexist = ClassRoutine.objects.filter(ClassRoom=classroom,subject=subject,teacher=teacher,start=start,end=end)
        if not isexist:
            ClassRoutine.objects.create(ClassRoom=classroom,subject=subject,teacher=teacher,start=start,end=end)
            return redirect('main:routinelist')
    
    context = {
        'classrooms':classrooms,
        'teachers':teachers,
        'subjects':subjects
    }

    return render(request,'createroutine.html',context)


def deleteroutine(request,routineid):
    ClassRoutine.objects.filter(routineid=routineid).delete()
    return redirect('main:routinelist')