from django import forms
from .models import *

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields=["email"]

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email'})


class ProfileSignupForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields=["name","contact_number"]


    def __init__(self, *args, **kwargs):
        super(ProfileSignupForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name'})
        self.fields['contact_number'].widget.attrs.update({'placeholder': 'Your Contact Number'})


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields=["email","password"]

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Your Password'})