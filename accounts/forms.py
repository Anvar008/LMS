from django import forms
from django.core.exceptions import ValidationError

from .models import *


class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password']

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password do not match')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()

        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())

class NewUser(forms.ModelForm):
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['role',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password']

        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Passwords do not match')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()

        return user


class TeacherProfile(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['experience',
                  'phone_number',
                  'avatar',
                  'bio']

        widgets = {
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }


class StudentProfile(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['study_place',
                  'phone_number',
                  'address',
                  'avatar',
                  'bio']

        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'study_place': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }
