from django.shortcuts import render

from .models import Course

from learning.models import Lesson, LessonProgress

#コースの一覧を表示するビュー
def course_list(request):

    courses = Course.objects.all()

    course_data = []

    for course in courses:

        total_lessons = course.lesson_set.count()

        completed_lessons = LessonProgress.objects.filter(

            user=request.user,

            lesson__course=course,

            completed=True

        ).count()

        if total_lessons > 0:

            progress = int(
                completed_lessons / total_lessons * 100
            )

        else:

            progress = 0

        course_data.append({

            "course": course,

            "progress": progress,

            "total_lessons": total_lessons,

            "completed_lessons": completed_lessons,

        })

    return render(

        request,

        "courses/course_list.html",

        {

            "course_data": course_data

        }

    )

#コースの詳細とそのコースに属するレッスンの一覧を表示するビュー
def course_detail(request, course_id):

    course = Course.objects.get(id=course_id)

    lessons = Lesson.objects.filter(course=course).order_by('order')

    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})
# Create your views here.
