from django.db import models
from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import User
from adverts.models import *
import datetime
from django.forms import ModelForm, Textarea, TextInput, NumberInput, FileField, CheckboxInput, Select 
# from django.forms.extras.widgets import Select, SelectDateWidget
from pyuploadcare.dj.models import ImageGroupField, ImageField
from cloudinary.forms import CloudinaryFileField


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(attrs={'class': u'form-control','placeholder': u'Enter First Name', 'required': True}),
            'last_name': TextInput(attrs={'class': u'form-control','placeholder': u'Enter Last Name', 'required': True}),
            'email': TextInput(attrs={'class': u'form-control','placeholder': u'Enter Email', 'required': True}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name is not None and first_name is not '':
            return first_name
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name is not None and last_name is not '':
            return last_name
        else:
            raise forms.ValidationError("Cannot be blank")

    def clean_email(self):
        email = self.cleaned_data['email']
        if email is not None and email is not '':
            return email
        else:
             raise forms.ValidationError("Cannot be blank")

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        
       
        try:
            email = cleaned_data.get("email")
            user = User.objects.get(email=email)
            if user != self.instance:
                raise forms.ValidationError("Email already exists")
        except User.DoesNotExist:
            pass

class PostadForm(forms.ModelForm):
    image = CloudinaryFileField(required=False,

        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'item profile'
       },
    )
    class Meta:
        model = Advert
        fields = { 'name', 'description', 'price', 'location', 'category',  'item_condition','accept_terms', 'option', 'image'}
        labels = {
            'name' :'name',
            'accept_terms': 'accept_terms',
            'description' : 'description',
            'price': 'price',
            'location' : 'location',
            'category': 'category',
            'item_condition': 'item_condition', 
            'option': 'option',
          
            
     }


    def clean_price(self):
        price = self.cleaned_data['price']
        print(price)
        if price < 1 or price is "":
            raise forms.ValidationError("Item Price can not be blank")
        else:
            return price
            
    
class ReviewAdForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review']
        
        # widgets = {'reviewer': forms.HiddenInput(),'adseller': forms.HiddenInput()}

                   
     
        