from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib import messages
from django.shortcuts import redirect, render
from random import randrange

from teachers.models import Teacher
from faker import Faker
from .forms import TeacherForm
from django.shortcuts import render
from students.models import Student


# def generate_teachers(request):
#     # Generates fake teachers in specified quantity, 1 in default
#     cnt = request.GET.get('count')
#     if cnt is None:
#         cnt = 1
#     elif cnt not in [str(i) for i in range(101)]:
#         return HttpResponse('Wrong input')
#     fake = Faker()
#     res = ''
#     for i in range(int(cnt)):
#         fake_teacher = {
#             'first_name': fake.first_name(),
#             'last_name': fake.last_name(),
#             'age': fake.random_int(min=18, max=100)
#         }
#         teacher = Teacher(**fake_teacher)
#         teacher.save()
#         res += str(teacher) + '<br>'
#     res += str(cnt) + ' teachers created.'
#     return HttpResponse(res)


def generate_teacher(request, **kwargs):
    if kwargs == {}:
        cnt = 1
    else:
        cnt = kwargs['count']
    if cnt not in [i for i in range(101)]:
        return HttpResponse('Wrong input')
    group_names = ['python', 'java', 'VB']
    fake = Faker()
    for i in range(int(cnt)):
        fake_teacher = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': fake.random_int(min=18, max=100),
        }
        teacher = Teacher(**fake_teacher)
        teacher.save()
        new_group = teacher.group_set.create(name=group_names[randrange(len(group_names))],
                                             type=randrange(len(group_names)))
        for j in range(10):
            fake_student = {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'age': fake.random_int(min=18, max=100),
            }
            student = Student(**fake_student)
            student.save()
            new_group.students.add(student)

    return redirect('view-teachers')


def view_teachers(request):
    teachers_list = Teacher.objects.all()
    return render(request, 'teachers_list.html', {'teachers': teachers_list})


def create_teacher_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TeacherForm(request.POST)
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
            return HttpResponseRedirect('/teachers/view/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TeacherForm()

    return render(request, 'create_teacher.html', {'form': form})


def edit_teacher(request, teacher_id):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            Teacher.objects.update_or_create(defaults=form.cleaned_data, id=teacher_id)
            return HttpResponseRedirect(reverse('view-teachers'))
    else:
        teacher = Teacher.objects.filter(id=teacher_id).first()
        form = TeacherForm(model_to_dict(teacher))

    return render(request, 'edit_teacher.html', {'form': form, 'teacher_id': teacher_id})


def delete_teacher(request, teacher_id):
    Teacher.objects.filter(id=teacher_id).first().delete()
    return HttpResponseRedirect(reverse('view-teachers'))
