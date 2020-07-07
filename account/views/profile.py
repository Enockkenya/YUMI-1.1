from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
from django.shortcuts import render,redirect, get_object_or_404
from account.forms import UserForm,ClientForm
from registration.form import RegisterForm
from django.db import transaction
from account.models import *
from adverts.models import *
from django.contrib import messages
from django.utils.translation import gettext as _




@login_required(login_url='/home')
def view_profile(request):
    adverts = Advert.objects.filter(user_id=request.user.id)   
    return render(request, 'profile/profile_home.html',{
        'adverts':'adverts',
        'tab': 'profile',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required()
def update_user(request):
    response_data = {'status' : 'failed', 'message' : 'unknown deletion error'}
    if request.is_ajax():
        if request.method == 'POST':
            form = UserForm(instance=request.user, data=request.POST)
            if form.is_valid():
                form.instance.username = form.instance.email
                form.save()
                response_data = {'status' : 'success', 'message' : 'updated user'}
            else:
                response_data = {'status' : 'failed', 'message' : json.dumps(form.errors)}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required()
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':

        # user_form = RegisterForm(request.POST,instance=request.user)
        profile_form = ClientForm(request.POST,files=request.FILES, instance=request.user.client)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect ('account:view_my_ads', user_id = request.user.id )
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        profile_form = ClientForm(instance=request.user.client)
    return render(request, 'profile/edit_profile.html', {
        # 'user_form': user_form,
        'profile_form': profile_form,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


   

@login_required(login_url ='login:login_redirect')
def view_my_ads(request, user_id):
    adverts = Advert.objects.filter(user_id = request.user.id)   
    return render(request,'profile/myadds.html', context ={  
        'adverts': adverts,
        'user_id ': user_id, 
        'tab': 'adverts',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })

@login_required(login_url ='login:login_redirect')
def view_messages(request):
   
    return render(request, 'profile/messages.html',{
        
        'tab': 'messages',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })

@login_required(login_url ='login:login_redirect')
def view_who_watched(request):
   
    return render(request, 'profile/view_who_watched.html',{
        
        'tab': 'favourite',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })

@login_required(login_url ='login:login_redirect')
def view_saved_ads(request):
   
    return render(request, 'profile/savedads.html',{
        
        'tab': 'saved',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })

@login_required(login_url ='login:login_redirect')
def view_settings(request):
   
    return render(request, 'profile/settings.html',{
         
        'tab': 'settings',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })

