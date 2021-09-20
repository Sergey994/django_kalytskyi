from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "teacher_link", "students_link")
    list_filter = ("name", "type")
    search_fields = ("name__startswith", "type__startswith")

    def teacher_link(self, obj):
        return format_html('<a href="{}">{}</a>'.format(
            reverse("admin:teachers_teacher_change", args=(obj.teacher.pk,)),
            f"{obj.teacher.first_name} {obj.teacher.last_name}"
        ))

    def students_link(self, obj):
        res = ''
        for i in obj.students.all():
            res += i.first_name + ' ' + i.last_name + '\n'
        return res
