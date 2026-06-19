from django.shortcuts import render

from .models import Lesson,Slide,Quiz

from .forms import SubmissionForm

from .models import Submission, Result, LessonProgress

from .services import grade_excel

from .models import Assignment

#スライドの詳細を表示するビュー
def slide_detail(request, slide_id):

    slide = Slide.objects.get(id=slide_id)

    next_slide = Slide.objects.filter(lesson=slide.lesson, order__gt=slide.order).order_by('order').first()

    previous_slide = Slide.objects.filter(lesson=slide.lesson, order__lt=slide.order).order_by('-order').first()

    return render(request, 'learning/slide_detail.html', {'slide': slide, 'next_slide': next_slide, 'previous_slide': previous_slide})

#クイズの表示と回答の処理を行うビュー
def quiz_view(request, lesson_id):

    quiz = Quiz.objects.get(lesson_id=lesson_id)

    result = None
    
    if request.method == 'POST':

        answer = request.POST.get('answer')

        if answer == quiz.correct_answer:

            result = 'Correct!'

            LessonProgress.objects.update_or_create(

                user=request.user,

                lesson=quiz.lesson,

                defaults={"completed": True}
                
            )

        else:

            result = 'wow,Wrong!'
    
    return render(request, 'learning/quiz.html',{'quiz': quiz, 'result': result,})

#課題提出のビュー
def submission_view(request, lesson_id):

    lesson = Lesson.objects.get(id=lesson_id)

    if request.method == 'POST':

        form = SubmissionForm(request.POST, request.FILES)

        if form.is_valid():

            submission = form.save(commit=False)

            submission.lesson = lesson

            submission.save()
            
            score = grade_excel(submission.file.path,lesson)

            result = Result.objects.create(submission=submission, score=score)

            return render(request, "learning/result.html",{'result': result})         

    else:

        form = SubmissionForm()

    return render(request, "learning/submit_assignment.html", {'form': form})

def assignment_view(request, lesson_id):

    assignment = Assignment.objects.get(
        lesson_id=lesson_id
    )

    return render(
        request,
        "learning/assignment.html",
        {
            "assignment": assignment
        }
    )

def excel_practice(request, lesson_id):

    assignment = Assignment.objects.grt(
        lesson_id = lesson_id
    )

    return render(
        request,
        "learning/excel_practice.html",
        {
            "assignment": assignment
        }
    )
# Create your views here.