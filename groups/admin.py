from django.contrib import admin
from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    list_filter = ("name", "type")
    search_fields = ("name__startswith", "type__startswith")
