from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Teacher


@receiver(pre_save, sender=Teacher)
def capitalize_handler(sender, **kwargs):
    kwargs['instance'].first_name = kwargs['instance'].first_name.capitalize()
    kwargs['instance'].last_name = kwargs['instance'].last_name.capitalize()
