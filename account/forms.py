from django.db import models
from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import User
from account.models import PrivateMessage, UserProfile
# from account.models import Profile,Post
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm, Textarea, TextInput, NumberInput, FileField, Select
# from django.forms.extras.widgets import Select, SelectDateWidget
from cloudinary.forms import CloudinaryFileField


class PrivateMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ['from_address', 'title', 'text']
        labels = {
            'from_address': 'From',
        }


class UserProfileForm(forms.ModelForm):
    profile_pic = CloudinaryFileField(required=False,

        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'profilepic'
       },
      
    )
    class Meta:
        model = UserProfile
        fields = { 'profile_pic', 'county','bio', 'title', 'town', 'phone_number'}
        labels = {
            'county': 'County :',
            'phone_number' : 'phone_number',
            'bio': 'Bio :',
            'town':'town',
            'title':'title'   
            
     }

        widgets = { 
            'title' : TextInput(attrs={'class': u'form-control','placeholder': u'Enter First Name' }),
            'bio': TextInput(attrs={'class': u'form-control','placeholder': u'Enter your Bio here'}),
            'county': Select(attrs={'class': u'form-control'}),
            'town': Select(attrs={'class': u'form-control'}),
            'phone_number': NumberInput(attrs={'class': u'form-control','placeholder': u'Enter your age here'}),
        }

    