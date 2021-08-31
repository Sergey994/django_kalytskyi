from django.http import HttpResponse
from students.models import Student
from faker import Faker


def generate_student(request, **kwargs):
    if kwargs == {}:
        cnt = 1
    else:
        cnt = kwargs['count']
    if cnt not in [i for i in range(101)]:
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
