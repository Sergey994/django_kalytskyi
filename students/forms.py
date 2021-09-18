from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class StudentForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='age')

    phone_number_regex = RegexValidator(regex=r'\+380([0-9]){9}')
    phone = forms.CharField(validators=[phone_number_regex], label='Phone')


class ContactForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    message = forms.CharField(label='Message', max_length=100)

    email_regex = RegexValidator(regex=r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    email_from = forms.CharField(validators=[email_regex], label='Email')

