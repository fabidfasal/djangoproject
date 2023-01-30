from django import forms
from . models import Table1



class SignUpForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','class':'fas fa-user fa-lg me-3 fa-fw','placeholder':'Enter your password'}))
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','class':'fas fa-user fa-lg me-3 fa-fw','placeholder':'Re-Enter your password'}))
    class Meta():
        model=Table1
        fields="__all__"
    


class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)

    class Meta():
        model=Table1
        fields=('Email','Password')


class ChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)


class UpdateForm(forms.ModelForm):

    class Meta():
        model=Table1
        fields=('Name','Place','Age','Email')