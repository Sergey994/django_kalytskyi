from django.contrib import admin
from .models import Student


@admin.register(Student)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age")
    list_filter = ("first_name", "last_name", "age")
    search_fields = ("first_name__startswith", "last_name__startswith", "age")
