from django.db import models


class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
