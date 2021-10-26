from django.db import models
from .choices import CURRENCIES


class Student(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return f'#{self.id}: {self.first_name} {self.last_name}, {self.age}'


class Log(models.Model):
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    time = models.FloatField()
    created = models.CharField(max_length=200, blank=True)


class Exchange(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(max_length=4, choices=CURRENCIES)
    source = models.CharField(max_length=20, default='privatbank')
    buy_price = models.DecimalField(max_digits=19, decimal_places=5)
    sell_price = models.DecimalField(max_digits=19, decimal_places=5)

    def __str__(self):
        return f"{self.created_at}::{self.currency}, {self.source}, BUY: {self.buy_price}; SELL: {self.sell_price};"

