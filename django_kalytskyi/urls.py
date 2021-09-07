"""django_kalytskyi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from students.views import generate_student, create_student_form, view_students
from teachers.views import generate_teachers, create_teacher_form, \
    view_teachers
from groups.views import generate_groups, create_group_form, view_groups


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('groups/', include('groups.urls')),
    path('teachers/', include('teachers.urls'))
]
