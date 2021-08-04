from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from faker import Faker


def generate_student(request):
    cnt = request.GET.get('count')
    if cnt is None:
        cnt = 1
    elif cnt not in [str(i) for i in range(101)]:
        return HttpResponse('Wrong input')
    fake = Faker()
    res = ''
    for i in range(int(cnt)):
        fake_student = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': fake.random_int(min=18, max=100)
        }
        student = Student(**fake_student)
        student.save()
        res += str(student) + '<br>'
    res += str(cnt) + ' students created.'
    return HttpResponse(res)
