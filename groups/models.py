from django.db import models
from teachers.models import Teacher
from students.models import Student


class Group(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, null=True)

    def __str__(self):
        return f'{self.name}, {self.type}'
