from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError


from students.models import Student
from faker import Faker
from .forms import StudentForm
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
            'age': fake.random_int(min=18, max=100),
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
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'age': form.cleaned_data['age'],
                'phone': form.cleaned_data['phone']
            }
            if not data['phone'].isnumeric():
                raise ValidationError('Incorrect phone format')
            student = Student(**data)
            student.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/students/view/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'create_student.html', {'form': form})


def view_students(request):
    students_list = Student.objects.all()
    return render(request, 'students_list.html', {'students': students_list})


def edit_student(request, student_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
            return HttpResponseRedirect(reverse('view-students'))
    else:
        student = Student.objects.filter(id=student_id).first()
        form = StudentForm(model_to_dict(student))

    return render(request, 'edit_student.html', {'form': form, 'student_id': student_id})


def delete_student(request, student_id):
    Student.objects.filter(id=student_id).first().delete()
    return HttpResponseRedirect(reverse('view-students'))
