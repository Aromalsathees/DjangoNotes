from django import forms
from .models import *



# model form from django
class RegistarionForm(forms.ModelForm):

# ithu password input boxil kanathe irikkanu
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    email = forms.EmailField(
        label="user email"
    )

    class Meta:
        model = CustomUser
        fields = ['username','first_name','email','password','phone_number','addess']


# forms.form from django
class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )