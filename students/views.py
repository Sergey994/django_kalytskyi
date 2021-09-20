from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib import messages
from django.shortcuts import redirect, render


from students.models import Student, Log
from .forms import StudentForm, ContactForm

from .tasks import generate_stud, contact_mail

import datetime


def generate_student(request, **kwargs):
    if kwargs == {}:
        cnt = 1
    else:
        cnt = kwargs['count']
    if cnt not in [i for i in range(101)]:
        return HttpResponse('Wrong input')
    generate_stud.delay(cnt)
    messages.success(request, 'We are generating your random users! Wait a moment and refresh this page.')
    return redirect('view-students')


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
        student_groups = student.group_set.all()
        groups = []
        for group in student_groups:
            groups.append(group)
        form = StudentForm(model_to_dict(student))

    return render(request, 'edit_student.html', {'form': form, 'student_id': student_id, 'groups': groups})


def delete_student(request, student_id):
    Student.objects.filter(id=student_id).first().delete()
    return HttpResponseRedirect(reverse('view-students'))


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = {
                'title': form.cleaned_data['title'],
                'message': form.cleaned_data['message'],
                'email_from': form.cleaned_data['email_from'],
            }
            contact_mail.delay(data)
            messages.success(request, 'Mail is sent')

            return HttpResponseRedirect(reverse('view-students'))
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
