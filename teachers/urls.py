from django.urls import path, include

from .views import (
    generate_teachers,
    create_teacher_form,
    view_teachers,
    edit_teacher,
    delete_teacher
)

urlpatterns = [
    path('generate/', generate_teachers, name='generate-teachers'),
    path('view/', view_teachers, name='view-teachers'),
    path('create/', create_teacher_form, name='create-teacher'),
    path('edit<int:teacher_id>', edit_teacher, name='edit-teacher'),
    path('delete<int:teacher_id>', delete_teacher, name='delete-teacher'),
]
