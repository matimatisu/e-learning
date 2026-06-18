from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from courses.models import Course
from learning.models import LessonProgress

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('email')

        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/dashboard/')

    return render(
        request,
        'accounts/login.html'
    )

def dashboard(request):

    total_courses = Course.objects.count()

    completed_lessons = LessonProgress.objects.filter(

        user = request.user,
        
        completed=True
    
    ).count()

    total_lessons = 0

    for course in Course.objects.all():

        total_lessons += course.lesson_set.count()

    remaining_lessons = total_lessons - completed_lessons

    return render(

        request,

         "accounts/dashboard.html",

        {
            "total_courses": total_courses,
            "completed_lessons": completed_lessons,
            "remaining_lesson": remaining_lessons,
        }

    )

