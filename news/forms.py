from django import forms
from .models import *

class AddNewsCategory(forms.ModelForm):
    class Meta:
        model = NewsCategory
        fields = ['title']


class AddNews(forms.ModelForm):
    class Meta:
        model = New
        fields = ['category',
                  'title',
                  'image',
                  'description']
