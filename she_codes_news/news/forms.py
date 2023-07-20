# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory
class StoryForm(ModelForm):
    class Meta:        
        model = NewsStory        
        fields = ['title', 'pub_date', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                               format='%m/%d/%Y',
               attrs={
                   'class':'form-control',
                   'placeholder':'Select a date',
                   'type':'date'
               }
           ),
       }
                
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerUserCreationForm(UserCreationForm):
    # Add any additional fields or customization here if needed
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields
