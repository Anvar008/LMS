from django import forms
from django.http import HttpResponseForbidden

from .models import *

class AddCourseCategory(forms.ModelForm):
    class Meta:
        model = CourseCategory
        fields = ['title']


class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category',
                  'title',
                  'image',
                  'description',
                  'price',
                  'duration']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['teacher',
                  'title',
                  'course',
                  'max_students',
                  'start_time',
                  'finish_time',
                  'is_active']

class AddGroupStudent(forms.Form):
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all())
