from django.urls import path
from . import views

urlpatterns=[

    path('slide/<int:slide_id>/', views.slide_detail, name='slide_detail'),

    path('quiz/<int:lesson_id>/', views.quiz_view, name='quiz'),

    path('submit/<int:lesson_id>/', views.submission_view, name='submit_assignment'),

]