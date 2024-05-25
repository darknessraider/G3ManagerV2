from django import forms

class UserSignupForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=30)
    email = forms.CharField(label="Email", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", max_length=30)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password", max_length=30)



