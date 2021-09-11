from django import forms
from django.core.exceptions import ValidationError


class StudentForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='age')
    phone = forms.CharField(label='Phone', max_length=13)

    def checkPhone(self):
        if not self.cleaned_data['phone'].isnumeric():
            raise ValidationError('Incorrect phone format')
        return
