from celery import shared_task
from .models import Student, Log
from faker import Faker
import datetime

from django.core.mail import send_mail


@shared_task()
def generate_stud(cnt):
    fake = Faker()
    res = ''
    for i in range(int(cnt)):
        fake_student = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': fake.random_int(min=18, max=100),
        }
        student = Student(**fake_student)
        student.save()
        res += str(student) + '<br>'
    res += str(cnt) + ' students created.'
    return res


@shared_task()
def contact_mail(data):
    send_mail(subject=data['title'], message=data['message'],
              recipient_list=[data['email_from']], fail_silently=False)


@shared_task()
def delete_logs():
    logs = Log.objects.all()
    for log in logs:
        if (datetime.datetime.now() - datetime.datetime.strptime(log.created, '%m/%d/%Y, %H:%M:%S')) > datetime.timedelta(7):
            log.delete()
