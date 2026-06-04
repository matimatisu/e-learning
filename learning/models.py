from django.db import models

from courses.models import Course

class Lesson(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    order = models.IntegerField()

    def __str__(self):

        return self.title
    
class Slide(models.Model):

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    content = models.TextField()

    order = models.IntegerField()

    def __str__(self):

        return self.title
    
class Quiz(models.Model):

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    
    question = models.TextField()

    choice_1 = models.CharField(max_length=100)

    choice_2 = models.CharField(max_length=100)

    choice_3 = models.CharField(max_length=100)

    correct_answer = models.CharField(max_length=100)

    explanation = models.TextField()

    def __str__(self):

        return self.question
    
class Submission(models.Model):
    
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    file = models.FileField(upload_to = 'submissions/')

    sumitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.lesson.title}"
    

#採点結果を保存するモデル    
class Result(models.Model):

    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)

    score = models.IntegerField()

    feedback = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.score}点"

# Create your models here.
