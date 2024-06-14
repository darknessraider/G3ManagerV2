from django import forms
from django.contrib.auth.models import User

class CreateTodoitemForm(forms.Form):
    name = forms.CharField(max_length=30)

