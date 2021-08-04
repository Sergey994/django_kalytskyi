from django.http import HttpResponse
from groups.models import Group


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
