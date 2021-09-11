from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib import messages
from django.shortcuts import redirect, render

from django.dispatch import receiver



from groups.models import Group
from .forms import GroupForm


def generate_groups(request):
    # Generates groups by list
    res = ''
    group_names = ['python', 'java', 'VB']
    for i in range(len(group_names)):
        fake_group = {
            'name': group_names[i - 1],
            'type': i,
        }
        group = Group(**fake_group)
        group.save()
        res += str(group) + '<br>'
    res += str(len(group_names)) + ' groups created.'
    return HttpResponse(res)


def view_groups(request):
    groups_list = Group.objects.all()
    return render(request, 'groups_list.html', {'groups': groups_list})


def create_group_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GroupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'type': form.cleaned_data['type'],
            }
            group = Group(**data)
            group.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/groups/view/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GroupForm()

    return render(request, 'create_group.html', {'form': form})


def edit_group(request, group_id):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            Group.objects.update_or_create(defaults=form.cleaned_data, id=group_id)
            return HttpResponseRedirect(reverse('view-groups'))
    else:
        group = Group.objects.filter(id=group_id).first()
        form = GroupForm(model_to_dict(group))

    return render(request, 'edit_group.html', {'form': form, 'group_id': group_id})


def delete_group(request, group_id):
    Group.objects.filter(id=group_id).first().delete()
    return HttpResponseRedirect(reverse('view-groups'))

