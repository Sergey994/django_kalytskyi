from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student


@receiver(pre_save, sender=Student)
def capitalize_handler(sender, **kwargs):
    kwargs['instance'].first_name = kwargs['instance'].first_name.capitalize()
    kwargs['instance'].last_name = kwargs['instance'].last_name.capitalize()
