from django import forms
from .models import Signup


class EmailSignUpForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "id": "emailHolder",
        "type": "email",
        "placeholder": "Email address"
    }), label="") 

    class Meta:
        model = Signup
        fields = ("email",)
