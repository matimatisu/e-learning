from django.contrib import admin
from .models import Lesson,Slide,Quiz,Submission,Result,LessonProgress,Assignment

admin.site.register(Lesson)
admin.site.register(Slide)
admin.site.register(Quiz)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(LessonProgress)
admin.site.register(Result)
