from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    final_grade = models.IntegerField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return self.name
