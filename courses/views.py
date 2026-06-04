from django.shortcuts import render

from .models import Course

from learning.models import Lesson
def course_list(request):

    courses = Course.objects.all()

    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):

    course = Course.objects.get(id=course_id)

    lessons = Lesson.objects.filter(course=course).order_by('order')

    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})
# Create your views here.
