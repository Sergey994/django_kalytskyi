from celery import shared_task
from .models import Student, Log, Exchange
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


import requests
from .choices import CURRENCIES


@shared_task()
def get_currency_rates_pb():
    exhange_response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    while True:
        exchange_result = exhange_response.json()
        for rate in exchange_result:
            if rate.get('ccy') not in [currency[0] for currency in CURRENCIES]:
                continue

            exchange = Exchange(
                currency=rate.get('ccy'),
                buy_price=rate.get('buy'),
                sell_price=rate.get('sale')
            )
            exchange.save()

        return 'Pb rates saved'


@shared_task()
def get_currency_rates_mb():
    exhange_response = requests.get('https://api.monobank.ua/bank/currency')
    # usd 840
    # eur 978
    # uah 980
    for i in exhange_response.json():
        if i['currencyCodeA'] == '840':
            exchange = Exchange(
                currency='USD',
                buy_price=i.get('rateBuy'),
                sell_price=i.get('rateSell')
            )
            exchange.save()
        elif i['currencyCodeA'] == '978':
            exchange = Exchange(
                currency='EUR',
                buy_price=i.get('rateBuy'),
                sell_price=i.get('rateSell')
            )
            exchange.save()

        return 'Mb rates saved'
