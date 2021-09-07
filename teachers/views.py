from django.http import HttpResponse, HttpResponseRedirect
from teachers.models import Teacher
from faker import Faker
from .forms import CreateTeacherForm
from django.shortcuts import render


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
    args = {}
    for i in request.GET.keys():
        args[i] = request.GET[i]
    res = ''
    for teacher in Teacher.objects.filter(**args):
        res += str(teacher) + '<br>'
    return HttpResponse(res)


def create_teacher_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateTeacherForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'age': form.cleaned_data['age']
            }
            teacher = Teacher(**data)
            teacher.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/view_teachers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateTeacherForm()

    return render(request, 'create_teacher.html', {'form': form})
