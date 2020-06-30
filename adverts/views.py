import json
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from adverts.forms import PostadForm
from adverts.models import *
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils.text import slugify


def view_post_ad(request):
    if request.method == 'POST':
       
         # user_form = RegisterForm(request.POST,instance=request.user)
        post_form = PostadForm(request.POST,files=request.FILES)
        
        if post_form.is_valid():
            post_form=post_form.save(commit=False)
            post_form.slug = slugify(post_form.name)
            post_form.user=request.user
            post_form.save()
            messages.success(request, _('Your ad was successfully posted!'))
            return redirect('/ads')

        else:
            messages.error(request, _('Please correct the error below.'))
    else:
         post_form = PostadForm(instance=request.user)
    return render(request, 'listings/postad.html', {
        # 'user_form': user_form,
        'post_form': post_form,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })

# @login_required(login_url='/accounts/login/')
def adverts_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    adverts = Advert.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        adverts = Advert.objects.filter(category=category)

   

    return render(request, 'listings/advertlist.html',   context = {
        'category': category,
        'categories': categories,
        'adverts': adverts, 
        'tab': 'listings',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


def advert_detail(request, id, slug):
    advert = get_object_or_404(Advert, id=id , slug=slug, available=True)
    return render( request, 'listings/advertdetail.html', context = {
        'advert': advert,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    }
      )

  

