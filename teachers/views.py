from django.http import HttpResponse
from teachers.models import Teacher
from faker import Faker


def generate_teachers(request):
    # Generates fake teachers in specified quantity, 1 in default
    cnt = request.GET.get('count')
    if cnt is None:
        cnt = 1
    elif cnt not in [str(i) for i in range(101)]:
        return HttpResponse('Wrong input')
    fake = Faker()
    res = ''
    for i in range(int(cnt)):
        fake_teacher = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': fake.random_int(min=18, max=100)
        }
        teacher = Teacher(**fake_teacher)
        teacher.save()
        res += str(teacher) + '<br>'
    res += str(cnt) + ' teachers created.'
    return HttpResponse(res)


def view_teachers(request):
    # Returns all teachers in db
    res = ''
    for teacher in Teacher.objects.order_by('first_name'):
        res += str(teacher) + '<br>'
    return HttpResponse(res)