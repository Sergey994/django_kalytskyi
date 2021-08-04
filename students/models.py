from django.db import models


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)

    def __str__(self):
        return f'#{self.id}: {self.first_name} {self.last_name}, {self.age}'