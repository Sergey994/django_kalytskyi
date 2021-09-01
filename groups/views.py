from django.http import HttpResponse, HttpResponseRedirect
from groups.models import Group
from .forms import CreateGroupForm
from django.shortcuts import render


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
    # Returns all the groups in db
    res = ''
    for group in Group.objects.order_by('name'):
        res += str(group) + '<br>'
    return HttpResponse(res)


def create_group_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateGroupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'type': form.cleaned_data['type'],
            }
            group = Group(**data)
            group.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/view_groups/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateGroupForm()

    return render(request, 'create_group.html', {'form': form})
