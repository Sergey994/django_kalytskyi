from django.urls import path, include

from .views import (
    generate_groups,
    create_group_form,
    view_groups,
    edit_group,
    delete_group
)

urlpatterns = [
    #path('generate/', generate_groups, name='generate-groups'),
    path('view/', view_groups, name='view-groups'),
    path('create/', create_group_form, name='create-group'),
    path('edit<int:group_id>', edit_group, name='edit-group'),
    path('delete<int:group_id>', delete_group, name='delete-group'),
    path('', view_groups)
]
