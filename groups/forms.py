from django import forms


class CreateGroupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    type = forms.CharField(label='Type', max_length=100)
