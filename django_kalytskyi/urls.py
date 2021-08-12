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
from django.urls import path
from students.views import generate_student
from teachers.views import generate_teachers
from teachers.views import view_teachers
from groups.views import generate_groups
from groups.views import view_groups


urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate_student/<int:count>', generate_student),
    path('generate_student/', generate_student),
    path('generate_teachers/', generate_teachers),
    path('view_teachers/', view_teachers),
    path('generate_groups/', generate_groups),
    path('view_groups/', view_groups),
]
