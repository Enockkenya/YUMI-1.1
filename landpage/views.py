import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
# from .models import Image,Profile,Comment,County
# from .forms import EditProfileForm
from django.contrib.auth.models import User
from account.models import *
from adverts.models import *

#landingpagemodel #home
def land_page (request, category_slug=None):
    category = None
    categories = Category.objects.all()
    adverts = Advert.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        adverts = Advert.objects.filter(category=category)
    return render(request, 'homepage/index.html',{
        'tab': 'land_page',
         'adverts' : adverts,
       
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

#clientwelcomepagemodel
def welcome(request):
    return render(request, 'homepage/welcome.html',{
        'tab': 'welcome',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })
#Aboutusmodel
def about_us(request):
    return render(request, 'homepage/aboutus.html',{
        'tab': 'aboutus',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def faqs(request):
    return render(request, 'homepage/faqs.html',{
        'tab': 'faqs',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def pricingtable(request):
    return render(request, 'homepage/Pricing.html',{
    'tab': 'pricing',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
     'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def contact_us(request):
    return render(request, 'homepage/contactus.html',{
        'tab': 'contactus',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })
