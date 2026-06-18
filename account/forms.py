from django import forms
from .models import *

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
        fields = ['first_name','email','password','phone_number','addess']