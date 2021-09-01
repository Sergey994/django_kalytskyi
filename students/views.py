from django.http import HttpResponse, HttpResponseRedirect
from students.models import Student
from faker import Faker
from .forms import CreateStudentForm
from django.shortcuts import render


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


def create_student_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateStudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'age': form.cleaned_data['age']
            }
            student = Student(**data)
            student.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/view_students/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateStudentForm()

    return render(request, 'create_student.html', {'form': form})


def view_students(request):
    args = {}
    for i in request.GET.keys():
        args[i] = request.GET[i]
    res = ''
    for student in Student.objects.filter(**args):
        res += str(student) + '<br>'
    return HttpResponse(res)
